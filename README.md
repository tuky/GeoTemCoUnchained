# GeoTemCoUnchained
Comparative visualization of geospatial-temporal data from your Django models.

GeoTemCo by Stefan Jänicke.
Django wrapping by Tobias Krönke.

## WARNING
This wrapper is still in dev. Not stable yet and no tests.

## Setup
Have `geotemco` in your `PYTHONPATH`, add it to your `INSTALLED_APPS`,
make sure, the templates in `geotemco` can be found and add
`url(r'^geotemco/', include('geotemco.urls'))` to your URL settings.

### Configuration
In your Django settings:
``` python
GEOTEMCO = {
    'data': {  # configure the data sources
        'users': {  # just a slug for the URL where to get the data
            'verbose': 'My Users',
            'queryset': 'app.geotemco.some_user_qs',  # dotted path to a qs
            'mapping': {  # maps from name in GeoTemCo to your respective model field name
                'lat': 'latitude',  # required
                'lon': 'longitude',  # required
                'place': 'location',  # required
                'time': 'created',  # required
                'description': 'title',  # required
                'pk': 'pk',  # optional
                '...': '...',  # can map anything and display it in GeoTemCo's table
            },
            'query_limit': 10000,  # optional limit applied to your queryset
        },
        ...
    },
    'title': u'This will be the title of the GeoTemCo View',
}
```

# GeoTemCo

##  GeoTemCo Introduction

The amount of online data annotated with geospatial and temporal metadata has grown rapidly in the recent years. Providers like Flickr and Twitter are popular, but hard to browse. Many systems exist that, in multiple linked views, show the data under geospatial, temporal, and topical aspects. GeoTemCo is a web-application which easily can be utilized to visualize such kind of data, and furthermore, it allows the comparative analysis of several datasets. GeoTemCo consists of several views showing the datas' several dimensions: a map view for the geospatial distribution of items, a time view for the temporal distribution of items and a detail view for the inspection of individual items. A broad range of interaction abilities allow the explorative comparison and analysis of different datasets representing different topics.

GeoTemCo focuses on supporting the user to:
* analyze and compare temporal trends
* analyze and compare geospatial distributions
* detect cooccurences between data items of different datasets
* compare geospatial migrations of topics over time
* find causalities between different datasets

## GeoTemCo Homepage

GeoTemCo is a project which is hosted at the University of Leipzig. You can find a tutorial, examples, projects using GeoTemCo, license information and contact details on our homepage: http://www.informatik.uni-leipzig.de/geotemco/

**If you are using GeoTemCo within your project, we kindly ask you to send us some details, so that we can keep our Projects page up-to-date.**
