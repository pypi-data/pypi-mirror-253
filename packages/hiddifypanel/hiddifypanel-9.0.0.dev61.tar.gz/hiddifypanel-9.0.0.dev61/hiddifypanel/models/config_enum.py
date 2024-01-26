from enum import auto

from strenum import StrEnum


class Lang(StrEnum):
    en = auto()
    fa = auto()
    ru = auto()
    pt = auto()
    zh = auto()


class ConfigCategory(StrEnum):
    admin = auto()
    branding = auto()
    general = auto()
    proxies = auto()
    domain_fronting = auto()
    telegram = auto()
    http = auto()
    tls = auto()
    mux = auto()
    tls_trick = auto()
    ssh = auto()
    ssfaketls = auto()
    shadowtls = auto()
    restls = auto()
    tuic = auto()
    hysteria = auto()
    ssr = auto()
    kcp = auto()
    hidden = auto()
    advanced = auto()
    too_advanced = auto()
    warp = auto()
    reality = auto()


class ConfigEnum(StrEnum):
    ssh_server_redis_url = auto()
    ssh_server_port = auto()
    ssh_server_enable = auto()
    first_setup = auto()
    core_type = auto()
    warp_enable = auto()
    warp_mode = auto()
    warp_plus_code = auto()
    warp_sites = auto()
    dns_server = auto()
    reality_fallback_domain = auto()
    reality_server_names = auto()
    reality_short_ids = auto()
    reality_private_key = auto()
    reality_public_key = auto()
    reality_port = auto()

    restls1_2_domain = auto()
    restls1_3_domain = auto()
    show_usage_in_sublink = auto()
    cloudflare = auto()
    license = auto()
    country = auto()
    package_mode = auto()
    utls = auto()
    telegram_bot_token = auto()
    is_parent = auto()
    parent_panel = auto()
    unique_id = auto()
    last_hash = auto()
    cdn_forced_host = auto()  # removed
    lang = auto()
    admin_lang = auto()
    admin_secret = auto()

    # tls
    tls_ports = auto()
    tls_fragment_enable = auto()
    tls_fragment_size = auto()
    tls_fragment_sleep = auto()
    tls_mixed_case = auto()
    tls_padding_enable = auto()
    tls_padding_length = auto()

    # mux
    mux_enable = auto()
    mux_protocol = auto()
    mux_max_connections = auto()
    mux_min_streams = auto()
    mux_max_streams = auto()
    mux_padding_enable = auto()
    mux_brutal_enable = auto()
    mux_brutal_up_mbps = auto()
    mux_brutal_down_mbps = auto()

    http_ports = auto()
    kcp_ports = auto()
    kcp_enable = auto()
    decoy_domain = auto()
    # will be deprecated
    proxy_path = auto()
    proxy_path_admin = auto()
    proxy_path_client = auto()
    firewall = auto()
    netdata = auto()
    http_proxy_enable = auto()
    block_iran_sites = auto()
    allow_invalid_sni = auto()
    auto_update = auto()
    speed_test = auto()
    only_ipv4 = auto()

    shared_secret = auto()

    telegram_enable = auto()
    # telegram_secret=auto()
    telegram_adtag = auto()
    telegram_lib = auto()
    telegram_fakedomain = auto()

    v2ray_enable = auto()
    torrent_block = auto()

    ssfaketls_enable = auto()
    # ssfaketls_secret="ssfaketls_secret"
    ssfaketls_fakedomain = auto()

    shadowtls_enable = auto()
    # shadowtls_secret=auto()
    shadowtls_fakedomain = auto()

    tuic_enable = auto()
    tuic_port = auto()

    # the hysteria is refereing to hysteria2
    hysteria_enable = auto()
    hysteria_port = auto()
    # if be enable hysteria2 will be use salamander as obfs
    hysteria_obfs_enable = auto()
    hysteria_up_mbps = auto()
    hysteria_down_mbps = auto()

    ssr_enable = auto()
    # ssr_secret="ssr_secret"
    ssr_fakedomain = auto()

    vmess_enable = auto()
    domain_fronting_domain = auto()
    domain_fronting_http_enable = auto()
    domain_fronting_tls_enable = auto()

    db_version = auto()

    branding_title = auto()
    branding_site = auto()
    branding_freetext = auto()
    not_found = auto()
    path_vmess = auto()
    path_vless = auto()
    path_trojan = auto()
    path_v2ray = auto()  # deprecated
    path_ss = auto()

    path_ws = auto()
    path_tcp = auto()
    path_grpc = auto()

    # cdn_forced_host=auto()
    @ classmethod
    def _missing_(cls, value):
        return cls.not_found  # "key not found"

    def info(self):
        map = {
            self.warp_sites: {'category': ConfigCategory.warp, 'apply_mode': 'apply'},
            self.ssh_server_redis_url: {'category': ConfigCategory.hidden},
            self.reality_port: {'category': ConfigCategory.reality, 'apply_mode': 'apply'},
            self.ssh_server_port: {'category': ConfigCategory.ssh, 'apply_mode': 'apply'},
            self.ssh_server_enable: {'category': ConfigCategory.ssh, 'type': bool, 'apply_mode': 'apply'},
            self.core_type: {'category': ConfigCategory.advanced, 'apply_mode': 'apply'},
            self.dns_server: {'category': ConfigCategory.general, 'apply_mode': 'apply'},
            self.warp_enable: {'category': ConfigCategory.hidden, 'type': bool, 'apply_mode': 'restart'},
            self.warp_mode: {'category': ConfigCategory.warp, 'apply_mode': 'apply'},
            self.warp_plus_code: {'category': ConfigCategory.warp, 'apply_mode': 'apply'},
            self.restls1_2_domain: {'category': ConfigCategory.hidden},
            self.restls1_3_domain: {'category': ConfigCategory.hidden},
            self.first_setup: {'category': ConfigCategory.hidden, 'type': bool},
            self.show_usage_in_sublink: {'category': ConfigCategory.general, 'type': bool},
            self.reality_fallback_domain: {'category': ConfigCategory.hidden, 'apply_mode': 'apply'},
            self.reality_server_names: {'category': ConfigCategory.hidden, 'apply_mode': 'apply'},
            self.reality_short_ids: {'category': ConfigCategory.reality, 'apply_mode': 'apply'},
            self.reality_private_key: {'category': ConfigCategory.reality, 'apply_mode': 'apply'},
            self.reality_public_key: {'category': ConfigCategory.reality, 'apply_mode': 'apply'},
            self.lang: {'category': ConfigCategory.branding, 'show_in_parent': True, 'commercial': True},
            self.admin_lang: {'category': ConfigCategory.admin, 'show_in_parent': True, 'commercial': True},
            self.cloudflare: {'category': ConfigCategory.too_advanced, 'commercial': True},
            self.license: {'category': ConfigCategory.hidden, 'commercial': True},
            self.proxy_path: {'category': ConfigCategory.hidden, 'apply_mode': 'apply', 'show_in_parent': True},
            self.proxy_path_admin: {'category': ConfigCategory.too_advanced, 'apply_mode': 'apply', 'show_in_parent': True},
            self.proxy_path_client: {'category': ConfigCategory.too_advanced, 'apply_mode': 'apply', 'show_in_parent': True},

            self.path_vmess: {'category': ConfigCategory.too_advanced},
            self.path_vless: {'category': ConfigCategory.too_advanced},
            self.path_trojan: {'category': ConfigCategory.too_advanced},
            self.path_ss: {'category': ConfigCategory.hidden},
            self.path_tcp: {'category': ConfigCategory.too_advanced},
            self.path_ws: {'category': ConfigCategory.too_advanced},
            self.path_grpc: {'category': ConfigCategory.too_advanced},
            self.path_v2ray: {'category': ConfigCategory.hidden},
            self.last_hash: {'category': ConfigCategory.hidden},

            self.utls: {'category': ConfigCategory.advanced, 'commercial': True},
            self.package_mode: {'category': ConfigCategory.advanced, 'show_in_parent': True, 'commercial': True},
            self.telegram_bot_token: {'category': ConfigCategory.telegram, 'show_in_parent': True, 'commercial': True},
            self.is_parent: {'category': ConfigCategory.hidden, 'type': bool},
            self.parent_panel: {'category': ConfigCategory.hidden, 'commercial': True},
            self.unique_id: {'category': ConfigCategory.hidden, },
            self.cdn_forced_host: {'category': ConfigCategory.hidden, },
            self.branding_title: {'category': ConfigCategory.branding, 'show_in_parent': True, 'commercial': True},
            self.branding_site: {'category': ConfigCategory.branding, 'show_in_parent': True, 'commercial': True},
            self.branding_freetext: {'category': ConfigCategory.branding, 'show_in_parent': True, 'commercial': True},
            self.not_found: {'category': ConfigCategory.hidden},
            self.admin_secret: {'category': ConfigCategory.hidden, 'show_in_parent': True, 'commercial': True},

            # tls
            self.tls_ports: {'category': ConfigCategory.tls, 'apply_mode': 'apply'},
            self.tls_fragment_enable: {'category': ConfigCategory.tls_trick, 'apply_mode': 'apply', 'type': bool},
            self.tls_fragment_size: {'category': ConfigCategory.tls_trick, 'apply_mode': 'apply'},
            self.tls_fragment_sleep: {'category': ConfigCategory.tls_trick, 'apply_mode': 'apply'},
            self.tls_mixed_case: {'category': ConfigCategory.tls_trick, 'apply_mode': 'apply', 'type': bool},
            self.tls_padding_enable: {'category': ConfigCategory.tls_trick, 'apply_mode': 'apply', 'type': bool},
            self.tls_padding_length: {'category': ConfigCategory.tls_trick, 'apply_mode': 'apply'},

            # mux
            self.mux_enable: {'category': ConfigCategory.mux, 'apply_mode': 'apply', 'type': bool},
            self.mux_protocol: {'category': ConfigCategory.mux, 'apply_mode': 'apply'},
            self.mux_max_connections: {'category': ConfigCategory.mux, 'apply_mode': 'apply'},
            self.mux_min_streams: {'category': ConfigCategory.mux, 'apply_mode': 'apply'},
            self.mux_max_streams: {'category': ConfigCategory.mux, 'apply_mode': 'apply'},
            self.mux_padding_enable: {'category': ConfigCategory.mux, 'apply_mode': 'apply', 'type': bool},
            self.mux_brutal_enable: {'category': ConfigCategory.mux, 'apply_mode': 'apply', 'type': bool},
            self.mux_brutal_up_mbps: {'category': ConfigCategory.mux, 'apply_mode': 'apply'},
            self.mux_brutal_down_mbps: {'category': ConfigCategory.mux, 'apply_mode': 'apply'},

            self.http_ports: {'category': ConfigCategory.http, 'apply_mode': 'apply'},  # http
            self.kcp_ports: {'category': ConfigCategory.hidden, 'apply_mode': 'apply'},
            self.kcp_enable: {'category': ConfigCategory.hidden, 'type': bool, 'apply_mode': 'apply'},
            self.decoy_domain: {'category': ConfigCategory.general, 'apply_mode': 'apply'},
            self.country: {'category': ConfigCategory.general, 'apply_mode': 'restart'},
            self.firewall: {'category': ConfigCategory.general, 'type': bool, 'apply_mode': 'apply'},
            self.netdata: {'category': ConfigCategory.hidden, 'type': bool, 'apply_mode': 'apply'},
            self.http_proxy_enable: {'category': ConfigCategory.http, 'type': bool},
            self.block_iran_sites: {'category': ConfigCategory.proxies, 'type': bool, 'apply_mode': 'apply'},
            self.allow_invalid_sni: {'category': ConfigCategory.tls, 'type': bool, 'apply_mode': 'apply'},
            self.auto_update: {'category': ConfigCategory.general, 'type': bool, 'apply_mode': 'apply', 'show_in_parent': True},
            self.speed_test: {'category': ConfigCategory.general, 'type': bool, 'apply_mode': 'apply'},
            self.only_ipv4: {'category': ConfigCategory.general, 'type': bool, 'apply_mode': 'apply'},
            self.torrent_block: {'category': ConfigCategory.general, 'type': bool, 'apply_mode': 'apply'},

            self.shared_secret: {'category': ConfigCategory.proxies, 'apply_mode': 'apply'},

            self.telegram_enable: {'category': ConfigCategory.telegram, 'type': bool, 'apply_mode': 'apply'},
            # telegram_secret:{'category':'general'},
            self.telegram_adtag: {'category': ConfigCategory.telegram, 'apply_mode': 'apply'},
            self.telegram_fakedomain: {'category': ConfigCategory.telegram, 'apply_mode': 'apply'},
            self.telegram_lib: {'category': ConfigCategory.telegram, 'apply_mode': 'reinstall'},

            self.v2ray_enable: {'category': ConfigCategory.hidden, 'type': bool, 'apply_mode': 'apply'},

            self.ssfaketls_enable: {'category': ConfigCategory.hidden, 'type': bool, 'apply_mode': 'apply'},
            # ssfaketls_secret:{'category':'ssfaketls'},
            self.ssfaketls_fakedomain: {'category': ConfigCategory.hidden, 'apply_mode': 'apply'},

            self.shadowtls_enable: {'category': ConfigCategory.shadowtls, 'type': bool, 'apply_mode': 'apply'},
            # shadowtls_secret:{'category':'shadowtls'},
            self.shadowtls_fakedomain: {'category': ConfigCategory.shadowtls, 'apply_mode': 'apply'},

            self.tuic_enable: {'category': ConfigCategory.hidden, 'type': bool, 'apply_mode': 'apply'},
            self.tuic_port: {'category': ConfigCategory.hidden, 'apply_mode': 'apply'},

            self.hysteria_enable: {'category': ConfigCategory.hidden, 'type': bool, 'apply_mode': 'apply'},
            self.hysteria_port: {'category': ConfigCategory.hidden, 'apply_mode': 'apply'},
            self.hysteria_obfs_enable: {'category': ConfigCategory.hysteria, 'type': bool, 'apply_mode': 'apply'},
            self.hysteria_up_mbps: {'category': ConfigCategory.hysteria, 'apply_mode': 'apply'},
            self.hysteria_down_mbps: {'category': ConfigCategory.hysteria, 'apply_mode': 'apply'},

            self.ssr_enable: {'category': ConfigCategory.hidden, 'type': bool, 'apply_mode': 'apply'},
            # ssr_secret:{'category':'ssr'},
            self.ssr_fakedomain: {'category': ConfigCategory.hidden, 'apply_mode': 'apply'},

            self.vmess_enable: {'category': ConfigCategory.proxies, 'type': bool},
            self.domain_fronting_domain: {'category': ConfigCategory.hidden},
            self.domain_fronting_http_enable: {'category': ConfigCategory.hidden, 'type': bool},
            self.domain_fronting_tls_enable: {'category': ConfigCategory.hidden, 'type': bool},
            self.db_version: {'category': ConfigCategory.hidden},
        }
        return map[self]

    def commercial(self):
        # print(self,self.info().get('commercial',False))
        return self.info().get('commercial', False)

    def category(self):
        return self.info()['category']

    def type(self):
        return self.info().get('type', str)

    def apply_mode(self):
        return self.info().get('apply_mode', '')

    def show_in_parent(self):
        return self.info().get('show_in_parent', False)
