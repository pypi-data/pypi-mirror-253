import datetime


from flask import render_template, url_for, request, jsonify, g, redirect
from hiddifypanel.panel.auth import login_required
from apiflask import abort
from flask_babelex import lazy_gettext as _
from flask_classful import FlaskView, route

import hiddifypanel
from hiddifypanel.models import *
from hiddifypanel.panel import hiddify
from hiddifypanel.panel.database import db
from hiddifypanel import hutils


class Dashboard(FlaskView):
    # TODO: delete this method
    # @login_required(roles={Role.admin})
    # def get_data(self):
    #     admin_id = request.args.get("admin_id") or g.account.id
    #     if admin_id not in g.account.recursive_sub_admins_ids():
    #         abort(403, _("Access Denied!"))

    #     return jsonify(dict(
    #         stats={'system': hiddify.system_stats(), 'top5': hiddify.top_processes()},
    #         usage_history=DailyUsage.get_daily_usage_stats(admin_id)
    #     ))

    @login_required(roles={Role.super_admin, Role.admin, Role.agent})
    def index(self):

        if hconfig(ConfigEnum.first_setup):
            return redirect(url_for("admin.QuickSetup:index"))
        if hiddifypanel.__release_date__ + datetime.timedelta(days=20) < datetime.datetime.now():
            hutils.flask.flash(_('This version of hiddify panel is outdated. Please update it from admin area.'), "danger")  # type: ignore
        bot = None
        # if hconfig(ConfigEnum.license):
        childs = None
        admin_id = request.args.get("admin_id") or g.account.id
        if admin_id not in g.account.recursive_sub_admins_ids():
            abort(403, _("Access Denied!"))

        child_id = request.args.get("child_id") or None
        user_query = User.query
        if admin_id:
            user_query = user_query.filter(User.added_by == admin_id)
        if hconfig(ConfigEnum.is_parent):
            childs = Child.query.filter(Child.id != 0).all()
            for c in childs:
                c.is_active = False
                for d in c.domains:
                    if d.mode == DomainType.fake:
                        continue
                    remote = hiddify.get_account_panel_link(g.account, d.domain, child_id=c.id)
                    d.is_active = hiddify.check_connection_to_remote(remote)
                    if d.is_active:
                        c.is_active = True

            # return render_template('parent_dash.html',childs=childs,bot=bot)
    # try:
        def_user = None if len(User.query.all()) > 1 else User.query.filter(User.name == 'default').first()
        domains = get_panel_domains()
        sslip_domains = [d.domain for d in domains if "sslip.io" in d.domain]

        if def_user and sslip_domains:
            quick_setup = url_for("admin.QuickSetup:index")
            hutils.flask.flash((_('It seems that you have not setup the system completely. <a class="btn btn-success" href="%(quick_setup)s">Click here</a> to complete setup.',
                                  quick_setup=quick_setup)), 'warning')  # type: ignore
            if hconfig(ConfigEnum.is_parent):
                hutils.flask.flash(_("Please understand that parent panel is under test and the plan and the condition of use maybe change at anytime."), "danger")  # type: ignore
        elif len(sslip_domains):
            hutils.flask.flash((_('It seems that you are using default domain (%(domain)s) which is not recommended.', domain=sslip_domains[0])), 'warning')  # type: ignore
            if hconfig(ConfigEnum.is_parent):
                hutils.flask.flash(_("Please understand that parent panel is under test and the plan and the condition of use maybe change at anytime."), "danger")  # type: ignore
        elif def_user:
            d = domains[0]
            hutils.flask.flash((_('It seems that you have not created any users yet. Default user link: %(default_link)s',
                               default_link=hiddify.get_html_user_link(def_user, d))), 'secondary')  # type: ignore
        if hiddify.is_ssh_password_authentication_enabled():
            hutils.flask.flash(_('ssh.password-login.warning.'), "warning")  # type: ignore

    # except:
    #     hutils.flask.flash((_('Error!!!')),'info')

        stats = {'system': hiddify.system_stats(), 'top5': hiddify.top_processes()}
        return render_template('index.html', stats=stats, usage_history=DailyUsage.get_daily_usage_stats(admin_id, child_id), childs=childs)

    @login_required(roles={Role.super_admin})
    @route('remove_child', methods=['POST'])
    def remove_child(self):
        child_id = request.form['child_id']
        child = Child.query.filter(Child.id == child_id).first()
        db.session.delete(child)
        db.session.commit()
        hutils.flask.flash(_("child has been removed!"), "success")  # type: ignore
        return self.index()
