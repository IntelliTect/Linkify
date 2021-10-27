import bs4

from linkify.linkify import Linkify
from linkify.posts import Post


def test__linkify__fix_a_href():
    link = "https://intellitect.com/demystifying-requirements-gathering/"
    replaced, actual = Linkify.fix_link(link)
    expected = "/demystifying-requirements-gathering/"
    assert replaced is True
    assert actual == expected


def test__linkify__fix_post_links():
    post = Post(
        "1",
        (
            '<!-- wp:heading -->\n<h2 id="h-sdets-automation-engineers-and-automated-ui-tests-won-t-save-you">You Need an SDET Unicorn: Automation Engineers, and Automated UI Tests Won\'t Save You. </h2>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>I have a potentially controversial opinion about my job. The popular concept of the Software Development Engineer in Test (SDET) role is broken for modern development practices.</p>\n<!-- /wp:paragraph -->\n<p>I don’t say that lightly. After thirteen years in the industry and eight of those years focused on automation, I’ve lived through the shift to agile practices.</p>\n<!-- wp:paragraph -->\n<p>At best, rather than empower an agile team that may also be striving for a DevOps culture, SDETs are often just another silo that contributes to quality (ensuring correctness and completeness of the application) only for regression testing. At worst, they slow the entire development process down for no measurable benefit.</p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>Imagine the mindset of a company. Picture finally moving to automation and the promises it brings, only to realize a year later that your SDET was just a three-day-long gate to the manual testers who did the same thing regardless of the SDET\'s work.</p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>Let\'s say your team can\'t keep up doing everything manually (a potentially regular occurrence for some), so you want to hire an SDET to help. What are the qualities of a modern, successful SDET?</p>\n<!-- /wp:paragraph -->\n<!-- wp:heading {"level":3} -->\n<h3 id="h-key-attributes-of-an-exemplary-sdet">Key Attributes of an Exemplary SDET</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>From a high level, I\'ve observed a few attributes in successful SDETs:</p>\n<!-- /wp:paragraph -->\n<ol>\n<li>They effectively grasp the quality needs of a broad range of stakeholders (developers, testers, business analysts, and even the customers*.) If not, they miss opportunities for quality improvement.</li>\n<li>They coach others on quality software attributes to affect multiple steps of the software development lifecycle. This is the only way they keep up with modern development demands.</li>\n<li>\n<p>They effectively communicate the benefits of their work. Otherwise, they risk perception as a &quot;typecast&quot; employee, nothing more than a &quot;code monkey&quot; who uncritically writes automated UI tests to fulfill someone else\'s asks instead of the organization\'s needs.</p></p>\n<p>*This has a huge caveat. I try to live my professional life by the adage, &quot;if it can be done, it will be done.&quot; It gets exponentially more challenging to analyze plausible customer interactions with a complex system and then distill that into 100% effective test cases. I often expect to fail with my first test suite. Also, I expect to refine it to understand better how the customer uses the system (either through reports from production or via exploratory testing by manual testers.)</p></p>\n<!-- /wp:paragraph -->\n</li>\n</ol>\n<p><img src="https://intellitect.com/wp-content/uploads/2021/08/MicrosoftTeams-image-7.jpg" alt="mike curn" /> <em>Mike Curn exemplifying the key attributes of a successful SDET in his work-from-home office.</em></p>\n<!-- wp:heading {"level":3} -->\n<h3 id="h-finding-a-unicorn">Finding an SDET Unicorn</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>Long story short, the concept of an SDET should be quality-focused with technical ability. "Quality" is not achieved solely through manual or automated UI (User Interface) tests. Rather, "quality" is achieved by understanding testing software at '
            'many layers of an application.</p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>This person might exist as <a href="https://devqa.io/sdet-hiring-software-developers-in-test/">somewhat of a unicorn</a>:</p>\n<!-- /wp:paragraph -->\n<!-- wp:quote -->\n<blockquote class="wp-block-quote"><p> "As well as participating in typical QA activities, they can write anything from automated integration tests, API tests, and/or UI automation tests.\n\nIn addition, SDETs could help review unit tests which are written by the developers \n\n… \n\nLet\'s be clear, an SDET is NOT an automation engineer. \n\nHaving the right balance of testing aptitude and technical skills is the key thing. \n\nA great SDET is a software tester by trade, is '
            'passionate about software quality and at the same time is tech-savvy and has the right mix of technical skills."</p><cite>Amir Ghahrai – <a href="https://devqa.io/sdet-hiring-software-developers-in-test/" target="_blank" rel="noreferrer noopener"><em>SDET Unicorns - Why is it so Hard to Hire SDETs?</em></a></cite></blockquote>\n<!-- /wp:quote -->\n<!-- wp:paragraph '
            '-->\n<p>Finding this "unicorn" is the challenge I see most frequently. Many in SDET positions either have the technical chops but not the testing mindset or the testing attitude but not the technical skill. To clarify, writing automated tests targeted at different layers of an application is not easy and is highly deliberate.</p>\n<!-- /wp:paragraph -->\n<!-- wp:heading {"level":3} -->\n<h3 id="h-the-sdet-origin-story">The SDET Origin Story</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>As the saying goes, "a defensive developer checks both ways before crossing a one-way street." </p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>Therefore, an SDET must help programmers check both ways before "crossing the street." Afterward, verifying that it was the right destination when they get to the other side.</p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>This is not a new concept. Microsoft has already had teams eliminate separate Dev and Test disciplines. </p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>This separation of disciplines is partly because of these challenges:</p>\n<!-- /wp:paragraph -->\n<!-- wp:quote -->\n<blockquote class="wp-block-quote"><p>"... full testing would take the better part of a day to run, many more hours to \'analyze the results\' to identify false failures, and days or weeks to repair all the tests that were broken due to some legitimate change in the product.\n\n<p>So, \xa0two years ago, we started on a path to completely redo testing.\xa0 We combined the dev and test orgs into a consolidating "engineering" org.\xa0 For the most part, we eliminated the distinction between people who code and people who test.\xa0 That\'s not to say every person does an identical amount of each, but every person does some of everything and is accountable for the quality of what they produce.”</p><cite>Brian Harry – <a href="https://devblogs.microsoft.com/bharry/testing-in-a-cloud-delivery-cadence/"><em>How we approach testing VSTS to enable continuous delivery</em></a></cite></blockquote>\n<!-- /wp:quote -->\n<!-- wp:paragraph -->\n<p>Say what you want about Microsoft\'s quality. </p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>After using TFS and VSTS (now Azure DevOps), I have not in recent memory seen a critical failure in that software due to their code. However, Microsoft still has some semblance of a test feedback loop via their preview releases, Insider program, and issues and feedback on their various channels like GitHub issues and <a href="https://docs.microsoft.com/en-us/answers/index.html">Microsoft Q&A</a>.</p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p><em>Note: according to the Dev community, Microsoft originated the acronym "SDET."</em></p>\n<!-- /wp:paragraph -->\n<!-- wp:heading {"level":3} -->\n<h3 id="h-mastering-the-sdet-role">Mastering the SDET Role</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>I am <em>not</em> advocating against any acceptance testing. Instead, I\'m arguing that <a href="https://danashby.co.uk/2016/10/19/continuous-testing-in-devops/" target="_blank" rel="noreferrer noopener">a successful SDET must empower quality at almost every step</a> in the software development process. Testing should be continuous.</p>\n<!-- /wp:paragraph -->\n<p>A quality specialist '
            'should be knowledgeable on many of the <a href="https://danashby.co.uk/2016/10/19/continuous-testing-in-devops/" target="_blank" rel="noreferrer noopener">steps Ashby mentions</a>. Maybe not all, but they need to have a grasp that quality permeates everything. More importantly, because &quot;everything&quot; is too much for one person to handle, an SDET needs to suggest, question, coach, and implement so that the whole team benefits at every step of software development.</p>\n<!-- wp:heading {"level":3} -->\n<h3 id="h-want-more">Want More?</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>What are some other qualities you\'ve seen in a successful SDET unicorn? Chime in, and we can build a list for finding new people for our teams!</p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>Also, check out <em><a href="https://intellitect.com/demystifying-requirements-gathering/" target="_blank" rel="noreferrer noopener">Demystifying the Requirements-Gathering Environment</a> </em>for more insight into improving your software lifecycle experience!</p>\n<!-- /wp:paragraph -->\n<p><a href="/join-our-team/" target="_blank" rel="noopener"></p>\n<p><img src="https://intellitect.com/wp-content/uploads/2021/04/Blog-job-ad-1024x127.png" alt="intellitect jobs ad" /></p>\n<p></a></p>'
        ),
        "post",
    )

    actual_post = Linkify().fix_post_links(post)
    actual = bs4.BeautifulSoup(actual_post.post_content, "html.parser")

    expected = bs4.BeautifulSoup(
        (
            '<!-- wp:heading -->\n<h2 id="h-sdets-automation-engineers-and-automated-ui-tests-won-t-save-you">You Need an SDET Unicorn: Automation Engineers, and Automated UI Tests Won\'t Save You. </h2>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>I have a potentially controversial opinion about my job. The popular concept of the Software Development Engineer in Test (SDET) role is broken for modern development practices.</p>\n<!-- /wp:paragraph -->\n<p>I don’t say that lightly. After thirteen years in the industry and eight of those years focused on automation, I’ve lived through the shift to agile practices.</p>\n<!-- wp:paragraph -->\n<p>At best, rather than empower an agile team that may also be striving for a DevOps culture, SDETs are often just another silo that contributes to quality (ensuring correctness and completeness of the application) only for regression testing. At worst, they slow the entire development process down for no measurable benefit.</p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>Imagine the mindset of a company. Picture finally moving to automation and the promises it brings, only to realize a year later that your SDET was just a three-day-long gate to the manual testers who did the same thing regardless of the SDET\'s work.</p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>Let\'s say your team can\'t keep up doing everything manually (a potentially regular occurrence for some), so you want to hire an SDET to help. What are the qualities of a modern, successful SDET?</p>\n<!-- /wp:paragraph -->\n<!-- wp:heading {"level":3} -->\n<h3 id="h-key-attributes-of-an-exemplary-sdet">Key Attributes of an Exemplary SDET</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>From a high level, I\'ve observed a few attributes in successful SDETs:</p>\n<!-- /wp:paragraph -->\n<ol>\n<li>They effectively grasp the quality needs of a broad range of stakeholders (developers, testers, business analysts, and even the customers*.) If not, they miss opportunities for quality improvement.</li>\n<li>They coach others on quality software attributes to affect multiple steps of the software development lifecycle. This is the only way they keep up with modern development demands.</li>\n<li>\n<p>They effectively communicate the benefits of their work. Otherwise, they risk perception as a &quot;typecast&quot; employee, nothing more than a &quot;code monkey&quot; who uncritically writes automated UI tests to fulfill someone else\'s asks instead of the organization\'s needs.</p></p>\n<p>*This has a huge caveat. I try to live my professional life by the adage, &quot;if it can be done, it will be done.&quot; It gets exponentially more challenging to analyze plausible customer interactions with a complex system and then distill that into 100% effective test cases. I often expect to fail with my first test suite. Also, I expect to refine it to understand better how the customer uses the system (either through reports from production or via exploratory testing by manual testers.)</p></p>\n<!-- /wp:paragraph -->\n</li>\n</ol>\n<p><img src="/wp-content/uploads/2021/08/MicrosoftTeams-image-7.jpg" alt="mike curn" /> <em>Mike Curn exemplifying the key attributes of a successful SDET in his work-from-home office.</em></p>\n<!-- wp:heading {"level":3} -->\n<h3 id="h-finding-a-unicorn">Finding an SDET Unicorn</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>Long story short, the concept of an SDET should be quality-focused with technical ability. "Quality" is not achieved solely through manual or automated UI (User Interface) tests. Rather, "quality" is achieved by understanding testing software at '
            'many layers of an application.</p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>This person might exist as <a href="https://devqa.io/sdet-hiring-software-developers-in-test/">somewhat of a unicorn</a>:</p>\n<!-- /wp:paragraph -->\n<!-- wp:quote -->\n<blockquote class="wp-block-quote"><p> "As well as participating in typical QA activities, they can write anything from automated integration tests, API tests, and/or UI automation tests.\n\nIn addition, SDETs could help review unit tests which are written by the developers \n\n… \n\nLet\'s be clear, an SDET is NOT an automation engineer. \n\nHaving the right balance of testing aptitude and technical skills is the key thing. \n\nA great SDET is a software tester by trade, is '
            'passionate about software quality and at the same time is tech-savvy and has the right mix of technical skills."</p><cite>Amir Ghahrai – <a href="https://devqa.io/sdet-hiring-software-developers-in-test/" target="_blank" rel="noreferrer noopener"><em>SDET Unicorns - Why is it so Hard to Hire SDETs?</em></a></cite></blockquote>\n<!-- /wp:quote -->\n<!-- wp:paragraph '
            '-->\n<p>Finding this "unicorn" is the challenge I see most frequently. Many in SDET positions either have the technical chops but not the testing mindset or the testing attitude but not the technical skill. To clarify, writing automated tests targeted at different layers of an application is not easy and is highly deliberate.</p>\n<!-- /wp:paragraph -->\n<!-- wp:heading {"level":3} -->\n<h3 id="h-the-sdet-origin-story">The SDET Origin Story</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>As the saying goes, "a defensive developer checks both ways before crossing a one-way street." </p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>Therefore, an SDET must help programmers check both ways before "crossing the street." Afterward, verifying that it was the right destination when they get to the other side.</p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>This is not a new concept. Microsoft has already had teams eliminate separate Dev and Test disciplines. </p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>This separation of disciplines is partly because of these challenges:</p>\n<!-- /wp:paragraph -->\n<!-- wp:quote -->\n<blockquote class="wp-block-quote"><p>"... full testing would take the better part of a day to run, many more hours to \'analyze the results\' to identify false failures, and days or weeks to repair all the tests that were broken due to some legitimate change in the product.\n\n<p>So, \xa0two years ago, we started on a path to completely redo testing.\xa0 We combined the dev and test orgs into a consolidating "engineering" org.\xa0 For the most part, we eliminated the distinction between people who code and people who test.\xa0 That\'s not to say every person does an identical amount of each, but every person does some of everything and is accountable for the quality of what they produce.”</p><cite>Brian Harry – <a href="https://devblogs.microsoft.com/bharry/testing-in-a-cloud-delivery-cadence/"><em>How we approach testing VSTS to enable continuous delivery</em></a></cite></blockquote>\n<!-- /wp:quote -->\n<!-- wp:paragraph -->\n<p>Say what you want about Microsoft\'s quality. </p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>After using TFS and VSTS (now Azure DevOps), I have not in recent memory seen a critical failure in that software due to their code. However, Microsoft still has some semblance of a test feedback loop via their preview releases, Insider program, and issues and feedback on their various channels like GitHub issues and <a href="https://docs.microsoft.com/en-us/answers/index.html">Microsoft Q&A</a>.</p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p><em>Note: according to the Dev community, Microsoft originated the acronym "SDET."</em></p>\n<!-- /wp:paragraph -->\n<!-- wp:heading {"level":3} -->\n<h3 id="h-mastering-the-sdet-role">Mastering the SDET Role</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>I am <em>not</em> advocating against any acceptance testing. Instead, I\'m arguing that <a href="https://danashby.co.uk/2016/10/19/continuous-testing-in-devops/" target="_blank" rel="noreferrer noopener">a successful SDET must empower quality at almost every step</a> in the software development process. Testing should be continuous.</p>\n<!-- /wp:paragraph -->\n<p>A quality specialist '
            'should be knowledgeable on many of the <a href="https://danashby.co.uk/2016/10/19/continuous-testing-in-devops/" target="_blank" rel="noreferrer noopener">steps Ashby mentions</a>. Maybe not all, but they need to have a grasp that quality permeates everything. More importantly, because &quot;everything&quot; is too much for one person to handle, an SDET needs to suggest, question, coach, and implement so that the whole team benefits at every step of software development.</p>\n<!-- wp:heading {"level":3} -->\n<h3 id="h-want-more">Want More?</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>What are some other qualities you\'ve seen in a successful SDET unicorn? Chime in, and we can build a list for finding new people for our teams!</p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>Also, check out <em><a href="/demystifying-requirements-gathering/" target="_blank" rel="noreferrer noopener">Demystifying the Requirements-Gathering Environment</a> </em>for more insight into improving your software lifecycle experience!</p>\n<!-- /wp:paragraph -->\n<p><a href="/join-our-team/" target="_blank" rel="noopener"></p>\n<p><img src="/wp-content/uploads/2021/04/Blog-job-ad-1024x127.png" alt="intellitect jobs ad" /></p>\n<p></a></p>'
        ),
        "html.parser",
    )

    assert actual == expected


def test__linkify__fix_post_links__returns_false_when_one_char_different():
    post = Post(
        "1",
        (
            '<!-- wp:heading -->\n<h2 id="h-sdets-automation-engineers-and-automated-ui-tests-won-t-save-you">You Need an SDET Unicorn: Automation Engineers, and Automated UI Tests Won\'t Save You. </h2>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>I have a potentially controversial opinion about my job. The popular concept of the Software Development Engineer in Test (SDET) role is broken for modern development practices.</p>\n<!-- /wp:paragraph -->\n<p>I don’t say that lightly. After thirteen years in the industry and eight of those years focused on automation, I’ve lived through the shift to agile practices.</p>\n<!-- wp:paragraph -->\n<p>At best, rather than empower an agile team that may also be striving for a DevOps culture, SDETs are often just another silo that contributes to quality (ensuring correctness and completeness of the application) only for regression testing. At worst, they slow the entire development process down for no measurable benefit.</p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>Imagine the mindset of a company. Picture finally moving to automation and the promises it brings, only to realize a year later that your SDET was just a three-day-long gate to the manual testers who did the same thing regardless of the SDET\'s work.</p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>Let\'s say your team can\'t keep up doing everything manually (a potentially regular occurrence for some), so you want to hire an SDET to help. What are the qualities of a modern, successful SDET?</p>\n<!-- /wp:paragraph -->\n<!-- wp:heading {"level":3} -->\n<h3 id="h-key-attributes-of-an-exemplary-sdet">Key Attributes of an Exemplary SDET</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>From a high level, I\'ve observed a few attributes in successful SDETs:</p>\n<!-- /wp:paragraph -->\n<ol>\n<li>They effectively grasp the quality needs of a broad range of stakeholders (developers, testers, business analysts, and even the customers*.) If not, they miss opportunities for quality improvement.</li>\n<li>They coach others on quality software attributes to affect multiple steps of the software development lifecycle. This is the only way they keep up with modern development demands.</li>\n<li>\n<p>They effectively communicate the benefits of their work. Otherwise, they risk perception as a &quot;typecast&quot; employee, nothing more than a &quot;code monkey&quot; who uncritically writes automated UI tests to fulfill someone else\'s asks instead of the organization\'s needs.</p></p>\n<p>*This has a huge caveat. I try to live my professional life by the adage, &quot;if it can be done, it will be done.&quot; It gets exponentially more challenging to analyze plausible customer interactions with a complex system and then distill that into 100% effective test cases. I often expect to fail with my first test suite. Also, I expect to refine it to understand better how the customer uses the system (either through reports from production or via exploratory testing by manual testers.)</p></p>\n<!-- /wp:paragraph -->\n</li>\n</ol>\n<p><img src="https://intellitect.com/wp-content/uploads/2021/08/MicrosoftTeams-image-7.jpg" alt="mike curn" /> <em>Mike Curn exemplifying the key attributes of a successful SDET in his work-from-home office.</em></p>\n<!-- wp:heading {"level":3} -->\n<h3 id="h-finding-a-unicorn">Finding an SDET Unicorn</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>Long story short, the concept of an SDET should be quality-focused with technical ability. "Quality" is not achieved solely through manual or automated UI (User Interface) tests. Rather, "quality" is achieved by understanding testing software at '
            'many layers of an application.</p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>This person might exist as <a href="https://devqa.io/sdet-hiring-software-developers-in-test/">somewhat of a unicorn</a>:</p>\n<!-- /wp:paragraph -->\n<!-- wp:quote -->\n<blockquote class="wp-block-quote"><p> "As well as participating in typical QA activities, they can write anything from automated integration tests, API tests, and/or UI automation tests.\n\nIn addition, SDETs could help review unit tests which are written by the developers \n\n… \n\nLet\'s be clear, an SDET is NOT an automation engineer. \n\nHaving the right balance of testing aptitude and technical skills is the key thing. \n\nA great SDET is a software tester by trade, is '
            'passionate about software quality and at the same time is tech-savvy and has the right mix of technical skills."</p><cite>Amir Ghahrai – <a href="https://devqa.io/sdet-hiring-software-developers-in-test/" target="_blank" rel="noreferrer noopener"><em>SDET Unicorns - Why is it so Hard to Hire SDETs?</em></a></cite></blockquote>\n<!-- /wp:quote -->\n<!-- wp:paragraph '
            '-->\n<p>Finding this "unicorn" is the challenge I see most frequently. Many in SDET positions either have the technical chops but not the testing mindset or the testing attitude but not the technical skill. To clarify, writing automated tests targeted at different layers of an application is not easy and is highly deliberate.</p>\n<!-- /wp:paragraph -->\n<!-- wp:heading {"level":3} -->\n<h3 id="h-the-sdet-origin-story">The SDET Origin Story</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>As the saying goes, "a defensive developer checks both ways before crossing a one-way street." </p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>Therefore, an SDET must help programmers check both ways before "crossing the street." Afterward, verifying that it was the right destination when they get to the other side.</p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>This is not a new concept. Microsoft has already had teams eliminate separate Dev and Test disciplines. </p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>This separation of disciplines is partly because of these challenges:</p>\n<!-- /wp:paragraph -->\n<!-- wp:quote -->\n<blockquote class="wp-block-quote"><p>"... full testing would take the better part of a day to run, many more hours to \'analyze the results\' to identify false failures, and days or weeks to repair all the tests that were broken due to some legitimate change in the product.\n\n<p>So, \xa0two years ago, we started on a path to completely redo testing.\xa0 We combined the dev and test orgs into a consolidating "engineering" org.\xa0 For the most part, we eliminated the distinction between people who code and people who test.\xa0 That\'s not to say every person does an identical amount of each, but every person does some of everything and is accountable for the quality of what they produce.”</p><cite>Brian Harry – <a href="https://devblogs.microsoft.com/bharry/testing-in-a-cloud-delivery-cadence/"><em>How we approach testing VSTS to enable continuous delivery</em></a></cite></blockquote>\n<!-- /wp:quote -->\n<!-- wp:paragraph -->\n<p>Say what you want about Microsoft\'s quality. </p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>After using TFS and VSTS (now Azure DevOps), I have not in recent memory seen a critical failure in that software due to their code. However, Microsoft still has some semblance of a test feedback loop via their preview releases, Insider program, and issues and feedback on their various channels like GitHub issues and <a href="https://docs.microsoft.com/en-us/answers/index.html">Microsoft Q&A</a>.</p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p><em>Note: according to the Dev community, Microsoft originated the acronym "SDET."</em></p>\n<!-- /wp:paragraph -->\n<!-- wp:heading {"level":3} -->\n<h3 id="h-mastering-the-sdet-role">Mastering the SDET Role</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>I am <em>not</em> advocating against any acceptance testing. Instead, I\'m arguing that <a href="https://danashby.co.uk/2016/10/19/continuous-testing-in-devops/" target="_blank" rel="noreferrer noopener">a successful SDET must empower quality at almost every step</a> in the software development process. Testing should be continuous.</p>\n<!-- /wp:paragraph -->\n<p>A quality specialist '
            'should be knowledgeable on many of the <a href="https://danashby.co.uk/2016/10/19/continuous-testing-in-devops/" target="_blank" rel="noreferrer noopener">steps Ashby mentions</a>. Maybe not all, but they need to have a grasp that quality permeates everything. More importantly, because &quot;everything&quot; is too much for one person to handle, an SDET needs to suggest, question, coach, and implement so that the whole team benefits at every step of software development.</p>\n<!-- wp:heading {"level":3} -->\n<h3 id="h-want-more">Want More?</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>What are some other qualities you\'ve seen in a successful SDET unicorn? Chime in, and we can build a list for finding new people for our teams!</p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>Also, check out <em><a href="https://intellitect.com/demystifying-requirements-gathering/" target="_blank" rel="noreferrer noopener">Demystifying the Requirements-Gathering Environment</a> </em>for more insight into improving your software lifecycle experience!</p>\n<!-- /wp:paragraph -->\n<p><a href="/join-our-team/" target="_blank" rel="noopener"></p>\n<p><img src="https://intellitect.com/wp-content/uploads/2021/04/Blog-job-ad-1024x127.png" alt="intellitect jobs ad" /></p>\n<p></a></p>'
        ),
        "post",
    )

    actual_post = Linkify().fix_post_links(post)
    actual = bs4.BeautifulSoup(actual_post.post_content, "html.parser")

    expected = bs4.BeautifulSoup(
        (
            '<!-- wp:heading -->\n<h2 id="h-sdets-automation-engineers-and-automated-ui-tests-won-t-save-you">You Need an SDET Unicorn: Automation Engineers, and Automated UI Tests Won\'t Save You. </h2>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>I have a potentially controversial opinion about my job. The popular concept of the Software Development Engineer in Test (SDET) role is broken for modern development practices.</p>\n<!-- /wp:paragraph -->\n<p>I don’t say that lightly. After thirteen years in the industry and eight of those years focused on automation, I’ve lived through the shift to agile practices.</p>\n<!-- wp:paragraph -->\n<p>At best, rather than empower an agile team that may also be striving for a DevOps culture, SDETs are often just another silo that contributes to quality (ensuring correctness and completeness of the application) only for regression testing. At worst, they slow the entire development process down for no measurable benefit.</p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>Imagine the mindset of a company. Picture finally moving to automation and the promises it brings, only to realize a year later that your SDET was just a three-day-long gate to the manual testers who did the same thing regardless of the SDET\'s work.</p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>Let\'s say your team can\'t keep up doing everything manually (a potentially regular occurrence for some), so you want to hire an SDET to help. What are the qualities of a modern, successful SDET?</p>\n<!-- /wp:paragraph -->\n<!-- wp:heading {"level":3} -->\n<h3 id="h-key-attributes-of-an-exemplary-sdet">Key Attributes of an Exemplary SDET</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>From a high level, I\'ve observed a few attributes in successful SDETs:</p>\n<!-- /wp:paragraph -->\n<ol>\n<li>They effectively grasp the quality needs of a broad range of stakeholders (developers, testers, business analysts, and even the customers*.) If not, they miss opportunities for quality improvement.</li>\n<li>They coach others on quality software attributes to affect multiple steps of the software development lifecycle. This is the only way they keep up with modern development demands.</li>\n<li>\n<p>They effectively communicate the benefits of their work. Otherwise, they risk perception as a &quot;typecast&quot; employee, nothing more than a &quot;code monkey&quot; who uncritically writes automated UI tests to fulfill someone else\'s asks instead of the organization\'s needs.</p></p>\n<p>*This has a huge caveat. I try to live my professional life by the adage, &quot;if it can be done, it will be done.&quot; It gets exponentially more challenging to analyze plausible customer interactions with a complex system and then distill that into 100% effective test cases. I often expect to fail with my first test suite. Also, I expect to refine it to understand better how the customer uses the system (either through reports from production or via exploratory testing by manual testers.)</p></p>\n<!-- /wp:paragraph -->\n</li>\n</ol>\n<p><img src="/wp-content/uploads/2021/08/MicrosoftTeams-image-7.jpg" alt="mike curn" /> <em>Mike Curn exemplifying the key attributes of a successful SDET in his work-from-home office.</em></p>\n<!-- wp:heading {"level":3} -->\n<h3 id="h-finding-a-unicorn">Finding an SDET Unicorn</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>Long story short, the concept of an SDET should be quality-focused with technical ability. "Quality" is not achieved solely through manual or automated UI (User Interface) tests. Rather, "quality" is achieved by understanding testing software at '
            'many layers of an application.</p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>This person might exist as <a href="https://devqa.io/sdet-hiring-software-developers-in-test/">somewhat of a unicorn</a>:</p>\n<!-- /wp:paragraph -->\n<!-- wp:quote -->\n<blockquote class="wp-block-quote"><p> "As well as participating in typical QA activities, they can write anything from automated integration tests, API tests, and/or UI automation tests.\n\nIn addition, SDETs could help review unit tests which are written by the developers \n\n… \n\nLet\'s be clear, an SDET is NOT an automation engineer. \n\nHaving the right balance of testing aptitude and technical skills is the key thing. \n\nA great SDET is a software tester by trade, is '
            'passionate about software quality and at the same time is tech-savvy and has the right mix of technical skills."</p><cite>Amir Ghahrai – <a href="https://devqa.io/sdet-hiring-software-developers-in-test/" target="_blank" rel="noreferrer noopener"><em>SDET Unicorns  - Why is it so Hard to Hire SDETs?</em></a></cite></blockquote>\n<!-- /wp:quote -->\n<!-- wp:paragraph '
            '-->\n<p>Finding this "unicorn" is the challenge I see most frequently. Many in SDET positions either have the technical chops but not the testing mindset or the testing attitude but not the technical skill. To clarify, writing automated tests targeted at different layers of an application is not easy and is highly deliberate.</p>\n<!-- /wp:paragraph -->\n<!-- wp:heading {"level":3} -->\n<h3 id="h-the-sdet-origin-story">The SDET Origin Story</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>As the saying goes, "a defensive developer checks both ways before crossing a one-way street." </p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>Therefore, an SDET must help programmers check both ways before "crossing the street." Afterward, verifying that it was the right destination when they get to the other side.</p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>This is not a new concept. Microsoft has already had teams eliminate separate Dev and Test disciplines. </p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>This separation of disciplines is partly because of these challenges:</p>\n<!-- /wp:paragraph -->\n<!-- wp:quote -->\n<blockquote class="wp-block-quote"><p>"... full testing would take the better part of a day to run, many more hours to \'analyze the results\' to identify false failures, and days or weeks to repair all the tests that were broken due to some legitimate change in the product.\n\n<p>So, \xa0two years ago, we started on a path to completely redo testing.\xa0 We combined the dev and test orgs into a consolidating "engineering" org.\xa0 For the most part, we eliminated the distinction between people who code and people who test.\xa0 That\'s not to say every person does an identical amount of each, but every person does some of everything and is accountable for the quality of what they produce.”</p><cite>Brian Harry – <a href="https://devblogs.microsoft.com/bharry/testing-in-a-cloud-delivery-cadence/"><em>How we approach testing VSTS to enable continuous delivery</em></a></cite></blockquote>\n<!-- /wp:quote -->\n<!-- wp:paragraph -->\n<p>Say what you want about Microsoft\'s quality. </p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>After using TFS and VSTS (now Azure DevOps), I have not in recent memory seen a critical failure in that software due to their code. However, Microsoft still has some semblance of a test feedback loop via their preview releases, Insider program, and issues and feedback on their various channels like GitHub issues and <a href="https://docs.microsoft.com/en-us/answers/index.html">Microsoft Q&A</a>.</p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p><em>Note: according to the Dev community, Microsoft originated the acronym "SDET."</em></p>\n<!-- /wp:paragraph -->\n<!-- wp:heading {"level":3} -->\n<h3 id="h-mastering-the-sdet-role">Mastering the SDET Role</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>I am <em>not</em> advocating against any acceptance testing. Instead, I\'m arguing that <a href="https://danashby.co.uk/2016/10/19/continuous-testing-in-devops/" target="_blank" rel="noreferrer noopener">a successful SDET must empower quality at almost every step</a> in the software development process. Testing should be continuous.</p>\n<!-- /wp:paragraph -->\n<p>A quality specialist '
            'should be knowledgeable on many of the <a href="https://danashby.co.uk/2016/10/19/continuous-testing-in-devops/" target="_blank" rel="noreferrer noopener">steps Ashby mentions</a>. Maybe not all, but they need to have a grasp that quality permeates everything. More importantly, because &quot;everything&quot; is too much for one person to handle, an SDET needs to suggest, question, coach, and implement so that the whole team benefits at every step of software development.</p>\n<!-- wp:heading {"level":3} -->\n<h3 id="h-want-more">Want More?</h3>\n<!-- /wp:heading -->\n<!-- wp:paragraph -->\n<p>What are some other qualities you\'ve seen in a successful SDET unicorn? Chime in, and we can build a list for finding new people for our teams!</p>\n<!-- /wp:paragraph -->\n<!-- wp:paragraph -->\n<p>Also, check out <em><a href="/demystifying-requirements-gathering/" target="_blank" rel="noreferrer noopener">Demystifying the Requirements-Gathering Environment</a> </em>for more insight into improving your software lifecycle experience!</p>\n<!-- /wp:paragraph -->\n<p><a href="/join-our-team/" target="_blank" rel="noopener"></p>\n<p><img src="/wp-content/uploads/2021/04/Blog-job-ad-1024x127.png" alt="intellitect jobs ad" /></p>\n<p></a></p>'
        ),
        "html.parser",
    )

    assert actual != expected
