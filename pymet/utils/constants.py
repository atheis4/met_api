import os


class Columns:
    ARTIST_ALPHA_SORT = 'artist_alpha_sort'
    ARTIST_BEGIN_DATE = 'artist_begin_date'
    ARTIST_DISPLAY_BIO = 'artist_display_bio'
    ARTIST_END_DATE = 'artist_end_date'
    ARTIST_NATIONALITY = 'artist_nationality'
    ARTIST_PREFIX = 'artist_prefix'
    ARTIST_ROLE = 'artist_role'
    ARTIST_SUFFIX = 'artist_suffix'
    CITY = 'city'
    CLASSIFICATION = 'classification'
    CREDIT_LINE = 'credit_line'
    CULTURE = 'culture'
    COUNTRY = 'country'
    COUNTY = 'county'
    DEPARTMENT = 'department'
    DIMENSIONS = 'dimensions'
    DYNASTY = 'dynasty'
    EXCAVATION = 'excavation'
    GEOGRAPHY_TYPE = 'geography_type'
    IS_HIGHLIGHT = 'is_highlight'
    IS_PUBLIC_DOMAIN = 'is_public_domain'
    LINK_RESOURCE = 'link_resource'
    LOCALE = 'locale'
    LOCUS = 'locus'
    MEDIUM = 'medium'
    METADATA_DATE = 'metadata_date'
    OBJECT_BEGIN_DATE = 'object_begin_date'
    OBJECT_DATE = 'object_date'
    OBJECT_END_DATE = 'object_end_date'
    OBJECT_ID = 'object_id'
    OBJECT_NAME = 'object_name'
    OBJECT_NUMBER = 'object_number'
    PERIOD = 'period'
    PORTFOLIO = 'portfolio'
    REGION = 'region'
    REIGN = 'reign'
    REPOSITORY = 'repository'
    RIGHTS_AND_REPRODUCTION = 'rights_and_reproduction'
    RIVER = 'river'
    STATE = 'state'
    SUBREGION = 'subregion'
    TAGS = 'tags'
    TITLE = 'title'

    ARTIST_COLUMNS = [
        ARTIST_ALPHA_SORT, ARTIST_BEGIN_DATE, ARTIST_END_DATE,
        ARTIST_NATIONALITY, CULTURE, COUNTRY, MEDIUM, OBJECT_BEGIN_DATE,
        OBJECT_END_DATE, OBJECT_ID, OBJECT_NAME, TAGS, TITLE
    ]


class CsvPaths:
    _ROOT_PATH = '/Users/Andrew/wip/art_crawl'
    COLLECTION = os.path.join(_ROOT_PATH, 'met_openaccess/MetObjects.csv')
    PAINTINGS = os.path.join(_ROOT_PATH, 'pymet/data/MetPaintings.csv')
