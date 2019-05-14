from tljh.hooks import hookimpl


@hookimpl
def tljh_extra_user_conda_packages():
    # FIXME: specify versions here.
    return [
        'r',
        'r-bh',
        'r-dbi',
        'r-ggally',
        'r-isocodes',
        'r-kernsmooth',
        'r-mass',
        'r-matrix',
        'r-nlp',
        'r-r6',
        'r-rcolorbrewer',
        'r-rodbc',
        'r-roracle',
        'r-rsqlite',
        'r-rcpp',
        'r-rgooglemaps',
        'r-snowballc',
        'r-askpass',
        'r-assertthat',
        'r-backports',
        'r-base',
        'r-base64enc',
        'r-bit',
        'r-bit64',
        'r-bitops',
        'r-blob',
        'r-boot',
        'r-broom',
        'r-callr',
        'r-cellranger',
        'r-chron',
        'r-class',
        'r-classint',
        'r-cli',
        'r-clipr',
        'r-cluster',
        'r-codetools',
        'r-colorspace',
        'r-compiler',
        'r-crayon',
        'r-crosstalk',
        'r-curl',
        'r-data.table',
        'r-datasets',
        'r-dbplyr',
        'r-digest',
        'r-dplyr',
        'r-dtt',
        'r-e1071',
        'r-ellipsis',
        'r-english',
        'r-evaluate',
        'r-fansi',
        'r-ff',
        'r-forcats',
        'r-foreach',
        'r-foreign',
        'r-fs',
        'r-generics',
        'r-ggplot2',
        'r-glue',
        'r-grdevices',
        'r-graphics',
        'r-grid',
        'r-gridextra',
        'r-gsubfn',
        'r-gtable',
        'r-haven',
        'r-hexbin',
        'r-highr',
        'r-hms',
        'r-htmltools',
        'r-htmlwidgets',
        'r-httpuv',
        'r-httr',
        'r-hunspell',
        'r-iterators',
        'r-janeaustenr',
        'r-jsonlite',
        'r-kableextra',
        'r-knitr',
        'r-labeling',
        'r-later',
        'r-lattice',
        'r-lazyeval',
        'r-leaflet',
        'r-lexicon',
        'r-lubridate',
        'r-magrittr',
        'r-maptools',
        'r-markdown',
        'r-memoise',
        'r-methods',
        'r-mgcv',
        'r-mgsub',
        'r-mime',
        'r-modelr',
        'r-munsell',
        'r-nlme',
        'r-nnet',
        'r-odbc',
        'r-openssl',
        'r-parallel',
        'r-pillar',
        'r-pkgconfig',
        'r-plogr',
        'r-plotly',
        'r-plyr',
        'r-png',
        'r-praise',
        'r-prettyunits',
        'r-processx',
        'r-progress',
        'r-promises',
        'r-proto',
        'r-ps',
        'r-purrr',
        'r-qdapregex',
        'r-raster',
        'r-readr',
        'r-readxl',
        'r-rematch',
        'r-reprex',
        'r-reshape',
        'r-reshape2',
        'r-rgdal',
        'r-rgeos',
        'r-rjson',
        'r-rlang',
        'r-rmarkdown',
        'r-rpart',
        'r-rprojroot',
        'r-rstudioapi',
        'r-rvest',
        'r-scales',
        'r-selectr',
        'r-sentimentr',
        'r-shiny',
        'r-slam',
        'r-sourcetools',
        'r-sp',
        'r-spatial',
        'r-splines',
        'r-splitstackshape',
        'r-sqldf',
        'r-stats',
        'r-stats4',
        'r-stopwords',
        'r-stringi',
        'r-stringr',
        'r-survival',
        'r-sys',
        'r-syuzhet',
        'r-tcltk',
        'r-testthat',
        'r-textclean',
        'r-textshape',
        'r-tibble',
        'r-tidyr',
        'r-tidyselect',
        'r-tidytext',
        'r-tinytex',
        'r-tokenizers',
        'rtools',
        'r-units',
        'r-utf8',
        'r-utils',
        'r-viridis',
        'r-viridislite',
        'r-webshot',
        'r-whisker',
        'r-withr',
        'r-xfun',
        'r-xml2',
        'r-xtable',
        'r-yaml',
        'r-zoo',
    ]
