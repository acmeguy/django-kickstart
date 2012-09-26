from django import template
import random

register = template.Library()

CORP_ICONS = [
    'icon-pinterest',
    'icon-google-plus',
    'icon-twitter',
    'icon-facebook',
    'icon-github',
    'icon-linkedin',
    'icon-google-plus-sign',
    'icon-twitter-sign',
    'icon-pinterest-sign',
    'icon-github-sign',
    ]

EDIT_ICONS = [
    'icon-italic',
    'icon-text-height',
    'icon-text-width',
    'icon-align-left',
    'icon-align-center',
    'icon-align-right',
    'icon-align-justify',
    'icon-list',
    'icon-indent-left',
    'icon-indent-right',
    'icon-font',
    'icon-bold',
    'icon-strikethrough',
    'icon-underline',
    'icon-table',
    'icon-copy',
    'icon-paste',
]

INTERNET_ICONS = [
    'icon-rss',
    'icon-link',
]

MEDIA_ICONS = [
    'icon-music',
    'icon-film',
    'icon-download',
    'icon-upload',
    'icon-facetime-video',
    'icon-picture',
    'icon-camera',
    'icon-camera-retro',
]

WEB_ICONS = [
    'icon-signout',
]

KNOWN_ICONS = [
    'icon-glass','icon-search','icon-envelope','icon-heart',
    'icon-star','icon-star-empty','icon-user','icon-th-large',
    'icon-th','icon-th-list','icon-ok:before','icon-remove','icon-zoom-in',
    'icon-zoom-out','icon-off:before','icon-signal','icon-cog','icon-trash',
    'icon-home','icon-file','icon-time','icon-road','icon-download-alt',
    'icon-inbox','icon-play-circle','icon-repeat',
    'icon-refresh','icon-list-alt','icon-lock','icon-flag','icon-headphones',
    'icon-volume-off','icon-volume-down','icon-volume-up','icon-qrcode','icon-barcode','icon-tag',
    'icon-tags','icon-book','icon-bookmark','icon-print',
    'icon-pencil','icon-map-marker','icon-adjust','icon-tint','icon-edit','icon-share','icon-check','icon-move',
    'icon-step-backward','icon-fast-backward','icon-backward','icon-play','icon-pause','icon-stop','icon-forward',
    'icon-fast-forward','icon-step-forward','icon-eject','icon-chevron-left','icon-chevron-right','icon-plus-sign',
    'icon-minus-sign','icon-remove-sign','icon-ok-sign','icon-question-sign','icon-info-sign','icon-screenshot',
    'icon-remove-circle','icon-ok-circle','icon-ban-circle','icon-arrow-left','icon-arrow-right','icon-arrow-up',
    'icon-arrow-down','icon-share-alt','icon-resize-full','icon-resize-small','icon-plus','icon-minus',
    'icon-asterisk','icon-exclamation-sign','icon-gift','icon-leaf','icon-fire','icon-eye-open','icon-eye-close',
    'icon-warning-sign','icon-plane','icon-calendar','icon-random','icon-comment','icon-magnet','icon-chevron-up',
    'icon-chevron-down','icon-retweet','icon-shopping-cart','icon-folder-close','icon-folder-open',
    'icon-resize-vertical''icon-resize-horizontal','icon-bar-chart','icon-facebook-sign',
    'icon-key','icon-cogs','icon-comments','icon-thumbs-up','icon-thumbs-down','icon-star-half',
    'icon-heart-empty','icon-linkedin-sign','icon-pushpin','icon-external-link','icon-signin',
    'icon-trophy','icon-upload-alt','icon-lemon','icon-phone','icon-check-empty',
    'icon-bookmark-empty','icon-phone-sign','icon-unlock',
    'icon-credit-card','icon-hdd','icon-bullhorn','icon-bell','icon-certificate','icon-hand-right',
    'icon-hand-left','icon-hand-up','icon-hand-down','icon-circle-arrow-left','icon-circle-arrow-right',
    'icon-circle-arrow-up','icon-circle-arrow-down','icon-globe','icon-wrench','icon-tasks','icon-filter',
    'icon-briefcase','icon-fullscreen','icon-group','icon-cloud','icon-beaker','icon-cut',
    'icon-paper-clip','icon-save','icon-sign-blank','icon-reorder','icon-list-ul','icon-list-ol',
    'icon-magic','icon-truck',
    'icon-money','icon-caret-down','icon-caret-up','icon-caret-left',
    'icon-caret-right','icon-columns','icon-sort','icon-sort-down','icon-sort-up','icon-envelope-alt',
    'icon-undo','icon-legal','icon-dashboard','icon-comment-alt','icon-comments-alt','icon-bolt','icon-sitemap',
    'icon-umbrella','icon-user-md'
]

ICON_SETS = {
    'web':WEB_ICONS,
    'internet':INTERNET_ICONS,
    'corp':CORP_ICONS,
    'media':MEDIA_ICONS,
    'edit':EDIT_ICONS,
}

@register.simple_tag
def random_icon(icon_set=None):
    return random.sample(ICON_SETS.get(icon_set,KNOWN_ICONS),1)[0]
