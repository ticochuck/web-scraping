from web_scraper import __version__
from web_scraper.scraper import wiki_page_parse, auto_search

wa_text = '''Confusion over the state of Washington and the city of Washington, D.C., led to renaming proposals during the statehood process for Washington in 1889, including David Dudley Field II's suggestion to name the new state "Tacoma". These proposals failed to garner support.[10] Washington, D.C.'s, own statehood movement in the 21st century includes a proposal to use the name "State of Washington, Douglass Commonwealth", which would conflict with the current state of Washington.[11] Residents of Washington (known as "Washingtonians") and the Pacific Northwest simply refer to the state as "Washington",[citation needed] and the nation's capital "Washington, D.C.", "the other Washington",[12] or simply "D.C."

Washington state has the 18th highest per capita effective tax rate in the United States, as of 2017.[citation needed] Their tax policy differs from neighboring Oregon's, which levies no sales tax, but does levy a personal income tax. This leads to border economic anomalies in the Portland-Vancouver metropolitan area.[112] Additional border economies exist with neighboring British Columbia and Idaho.[citation needed]

There are extensive waterways around Washington's largest cities, including Seattle, Bellevue, Tacoma and Olympia. The state highways incorporate an extensive network of bridges and the largest ferry system in the United States to serve transportation needs in the Puget Sound area. Washington's marine highway constitutes a fleet of twenty-eight ferries that navigate Puget Sound and its inland waterways to 20 different ports of call, completing close to 147,000 sailings each year. Washington is home to four of the five longest floating bridges in the world: the Evergreen Point Floating Bridge, Lacey V. Murrow Memorial Bridge and Homer M. Hadley Memorial Bridge over Lake Washington, and the Hood Canal Bridge which connects the Olympic Peninsula and Kitsap Peninsula. Among its most famous bridges is the Tacoma Narrows Bridge, which collapsed in 1940 and was rebuilt. Washington has a number of seaports on the Pacific Ocean, including Seattle, Tacoma, Kalama, Anacortes, Vancouver, Longview, Grays Harbor, Olympia, and Port Angeles.[citation needed]

The Cascade Mountain Range also impedes transportation. Washington operates and maintains roads over seven[vague] major mountain passes and eight minor passes. During winter months some of these passes are plowed, sanded, and kept safe with avalanche control. Not all stay open through the winter. The North Cascades Highway, State Route 20, closes every year due to snowfall and avalanches in the area of Washington Pass. The Cayuse and Chinook passes east of Mount Rainier also close in winter.[citation needed]

Washington is crossed by a number of freight railroads, and Amtrak's passenger Cascade route between Eugene, Oregon and Vancouver, BC is the eighth busiest Amtrak service in the U.S. Seattle's King Street Station, the busiest station in Washington, and 15th busiest in the U.S.,[125] serves as the terminus for the two long distance Amtrak routes in Washington, the Empire Builder to Chicago and the Coast Starlight to Los Angeles. The Sounder commuter rail service operates in Seattle and its surrounding cities, between Everett and Lakewood. The intercity network includes the Cascade Tunnel, the longest railroad tunnel in the United States, which is part of the Stevens Pass route on the BNSF Northern Transcom.[citation needed]

Sound Transit Link light rail currently operates in the Seattle area at a length of 20 miles (32 km), and in Tacoma at a length of 1.6 miles (2.6 km). The entire system has a funded expansion plan that will expand light rail to a total of 116 miles by 2041. Seattle also has a 3.8-mile (6.1 km) streetcar network with two lines and plans to expand further by 2025. Bus systems exist across the state, the busiest being King County Metro, located in Seattle and King County, with just above 122 million riders in 2017.[126] Residents of Vancouver have resisted proposals to extend Portland's mass transit system into Washington.[citation needed]

'''


def test_version():
    assert __version__ == '0.1.0'


def test_wiki_page_parse_exists():
    wiki_page_parse


def test_auto_search_exists():
    auto_search


def test_check_wiki_article_exists():
    wiki_page_parse.check_for_wiki_article
    

def test_get_citations_needed_count_exist():
    wiki_page_parse.get_citations_needed_count


def test_get_citations_needed_report_exist():
    wiki_page_parse.get_citations_needed_report


def test_get_citations_needed_count_usa():
    usa = wiki_page_parse('https://en.wikipedia.org/wiki/United_States')
    assert usa.get_citations_needed_count() == 5


def test_get_citations_needed_count_wa():
    wa = wiki_page_parse('https://en.wikipedia.org/wiki/Washington_(state)')
    assert wa.get_citations_needed_count() == 7


def test_get_citations_needed_count_kc():
    kc = wiki_page_parse('https://en.wikipedia.org/wiki/King_County,_Washington')
    assert kc.get_citations_needed_count() == 2


def test_get_citations_needed_report_wa():
    wa = wiki_page_parse('https://en.wikipedia.org/wiki/Washington_(state)')
    assert wa.get_citations_needed_report() == wa_text
    
    
def test_get_citations_needed_report_wa_first_30():
    wa = wiki_page_parse('https://en.wikipedia.org/wiki/Washington_(state)')
    actual = wa.get_citations_needed_report()
    expected = 'Confusion over the state of Wa'
    assert actual[:30] == expected
    

def test_get_citations_needed_report_usa_first_100():
    usa = wiki_page_parse('https://en.wikipedia.org/wiki/United_States')
    actual = usa.get_citations_needed_report()
    expected = 'After World War II, the United States and the Soviet Union competed for power, influence, and presti'
    assert actual[:100] == expected


def test_get_citations_needed_report_usa_last_200():
    usa = wiki_page_parse('https://en.wikipedia.org/wiki/United_States')
    actual = usa.get_citations_needed_report()
    expected = '''the disease has affected over 3 million Americans and killed over 130,000 people.[citation needed] The United States is, by far, the country with the most cases of COVID-19 as of June 10, 2020.[195]

'''
    assert actual[-200:] == expected


def test_check_wiki_article_false():
    invalid_search = wiki_page_parse('https://en.wikipedia.org/wiki/Cxvxczdfaff')
    assert invalid_search.check_for_wiki_article() == False


def test_check_wiki_article_true():
    invalid_search = wiki_page_parse('https://en.wikipedia.org/wiki/Costa_Rica')
    assert invalid_search.check_for_wiki_article() == True