 Searches for packages satisfying a given search criteria.

 This action accepts solr search query parameters (details below), and
 returns a dictionary of results, including dictized datasets that match
 the search criteria, a search count and also facet information.

    **Solr Parameters:**

 For more in depth treatment of each paramter,
please read the
    `Solr Documentation
    <https://lucene.apache.org/solr/guide/6_6/common-query-parameters.html>`
_.

 This action accepts a *subset* of solr's search query parameters:


    :param q: the solr query. Optional.
Default: ``\"*:*\"``
    :type q: string
    :param fq: any filter queries to apply. Note: ``+site_id:{ckan_site_id}``

 is added to this string prior to the query being executed.
    :type fq: string
    :param fq_list: additional
filter queries to apply.
    :type fq_list: list of strings
    :param sort: sorting of the search results. Optional.
Default:
        ``'score desc, metadata_modified desc'``. As per the solr
 documentation, this is a comma-separated
string of field names and
 sort-orderings.
    :type sort: string
    :param rows: the maximum number of matching
rows (datasets) to return.
        (optional, default: ``10``, upper limit: ``1000`` unless set in
 site's
configuration ``ckan.search.rows_max``)
    :type rows: int
    :param start: the offset in the complete result for
where the set of
 returned datasets should begin.
    :type start: int
    :param facet: whether to enable faceted
results. Default: ``True``.
    :type facet: string
    :param facet.mincount: the minimum counts for facet fields
should be
 included in the results.
    :type facet.mincount: int
    :param facet.limit: the maximum number of
values the facet fields return.
 A negative value means unlimited. This can be set instance-wide with
 the :
ref:`search.facets.limit` config option. Default is 50.
    :type facet.limit: int
    :param facet.field: the fields
to facet upon. Default empty. If empty,
 then the returned facet information is empty.
    :type facet.field: list of
strings
    :param include_drafts: if ``True``, draft datasets will be included in the
 results. A user will only be
returned their own draft datasets, and a
 sysadmin will be returned all draft datasets. Optional, the default
is
        ``False``.
    :type include_drafts: bool
    :param include_private: if ``True``, private datasets will
be included in
 the results. Only private datasets from the user's organizations will
 be returned and sysadmins will
be returned all private datasets.
 Optional, the default is ``False``.
    :type include_private: bool
    :param
use_default_schema: use default package schema instead of
 a custom schema defined with an IDatasetForm plugin (
default: ``False``)
    :type use_default_schema: bool


 The following advanced Solr parameters are supported as
well. Note that
 some of these are only available on particular Solr versions. See Solr's
    `dismax`_ and `edismax`_
documentation for further details on them:

    ``qf``, ``wt``, ``bf``, ``boost``, ``tie``, ``defType``, ``mm``



 .. _dismax: http://wiki.apache.org/solr/DisMaxQParserPlugin
    .. _
edismax: http://wiki.apache.org/solr/ExtendedDisMax


    **Examples:**

    ``q=flood`` datasets containing the
word `flood`, `floods` or `flooding`
    ``fq=tags:economy`` datasets with the tag `economy`

    ``facet.field=[\"tags\"] facet.limit=10 rows=0`` top 10 tags

    **Results:**

 The result of this action is
a dict with the following keys:

    :rtype: A dictionary with the following keys
    :param count: the number of
results found. Note, this is the total number
 of results found, not the total number of results returned (which is

affected by limit and row parameters used in the input).
    :type count: int
    :param results: ordered list of
datasets matching the query, where the
 ordering defined by the sort parameter used in the query.
    :type results:
list of dictized datasets.
    :param facets: DEPRECATED. Aggregated information about facet counts.
    :type facets:
DEPRECATED dict
    :param search_facets: aggregated information about facet counts. The outer
 dict is keyed by the
facet field name (as used in the search query).
 Each entry of the outer dict is itself a dict, with a \"title\" key,
and
 an \"items\" key. The \"items\" key's value is a list of dicts, each with
 \"count\", \"display_name\" and
\"name\" entries. The display_name is a
 form of the name that can be used in titles.
    :type search_facets: nested
dict of dicts.

 An example result: ::

 {'count': 2,
      'results': [ { <snip> }, { <snip> }],
      '
search_facets': {u'tags':
{'items': [{'count': 1,
                                             'display_name': u'tolstoy',
                                             'name': u'tolstoy'},
 {'count': 2,
                                             'display_name': u'russian',
                                             'name': u'russian'}
                                           ]

 }
 }
 }

    **Limitations:**

 The full solr query language is not exposed, including.

 fl
 The parameter
that controls which fields are returned in the solr
 query.
 fl can be None or a list of result fields, such
as ['id', 'extras_custom_field'].
 if fl = None, datasets are returned as a list of full dictionary.
    