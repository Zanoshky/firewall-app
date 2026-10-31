"""Builds the guide pages in docs/ from the bodies below, so they share one head, bar and footer, and refuses any
dash used as punctuation. python3 build.py"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).parent / 'docs'
PLAY = 'https://play.google.com/store/apps/details?id=com.zanoshky.firewall'
SITE = 'https://firewall.zanoski.com'
REPO = 'https://github.com/Zanoshky/firewall-app'
PAGES = [('index.html', 'Home'), ('guide.html', 'Guide'), ('faq.html', 'Questions'), ('report.html', 'Report a bug')]

def shell(file, title, desc, body):
    nav = ''.join(f'<a href="{f}"{" aria-current=\"page\"" if f == file else ""}>{n}</a>' for f, n in PAGES)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title} · Firewall user guide</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0c1116">
<meta property="og:title" content="{title} · Firewall user guide">
<meta property="og:description" content="{desc}">
<link rel="icon" href="img/icon-192.png" type="image/png">
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="bar">
  <div class="wrap">
    <a class="brand" href="index.html"><img src="img/icon-192.png" alt="" width="34" height="34"><span>Firewall</span></a>
    <nav aria-label="Guide pages">{nav}</nav>
  </div>
</header>
<main id="main" class="page">
  <div class="wrap">
{body}
  </div>
</main>
<footer>
  <div class="wrap">
    <span>Guide text and images are shared under CC BY 4.0. The Firewall app itself is proprietary. Made by Marko Zanoski.</span>
    <nav aria-label="Footer"><a href="{PLAY}">Google Play</a><a href="{SITE}">firewall.zanoski.com</a><a href="{REPO}/issues">Issues</a><a href="{SITE}/privacy">Privacy</a><a href="{SITE}/terms">Terms</a></nav>
  </div>
</footer>
</body>
</html>
'''

def shot(name, alt, cap):
    return f'<figure><img src="img/screen-{name}.webp" alt="{alt}" width="560" height="1152" loading="lazy"><figcaption>{cap}</figcaption></figure>'

INDEX = f'''    <p class="kicker">User guide</p>
    <h1>Firewall</h1>
    <p class="sub">A firewall for Android that needs no root, with tracker blocking, DNS over HTTPS, and a log of everything your phone looks up. You decide, app by app, what the firewall does with it. Free, with an optional Pro.</p>
    <div class="shots">
      {shot("apps", "The app list with lookups per app: Chrome, Calendar and Phosphor Filtered, Vinyl Blocked, and the bar at the bottom ending in Settings.", "Apps: Not filtered, Filtered or Blocked")}
      {shot("activity", "3.7K lookups, 1.0K blocked, 98% encrypted, and why lookups were stopped: tracker lists, your rules and blocked apps.", "Activity")}
      {shot("settings", "Settings: Look, then Protection with Encrypted lookups, Tracker lists, Your domain rules and New apps.", "Settings")}
      {shot("domains", "Your domain rules: a block list holding graph.facebook.com and tiktok.com, 2 of 3 free rules used.", "Your domain rules")}
      {shot("trackers", "Tracker lists: tracker blocking on with 129 names loaded, 848 blocked, and the memory the lists take.", "Tracker lists")}
    </div>
    <div class="cta">
      <a class="btn main" href="guide.html">Read the guide</a>
      <a class="btn" href="report.html">Report a bug or ask for a feature</a>
    </div>'''

GUIDE = '''    <p class="kicker">Guide</p>
    <h1>How Firewall works</h1>
    <article>
    <h2>What it does</h2>
    <p>Firewall runs a local VPN, but it does not carry your traffic. The tunnel claims one small, reserved range of addresses, and what comes through it is every name your phone looks up. A name that is blocked is answered with an address that goes nowhere, and the connection that follows is refused on the spot. A name that is allowed is resolved for real, encrypted if you asked for that. Your photos, video and downloads never enter the app, so nothing is slowed down and nothing keeps the processor awake.</p>
    <p>Turn it on with the switch in the card at the top of Home. The first time, Android asks you to allow the VPN, and then whether Firewall may send notifications. On a new install every app starts Filtered, with tracker blocking and encrypted lookups on, so apps work as before with trackers stopped.</p>
    <p>The bar at the bottom has four buttons: Home, Apps, Activity and Settings. Back from any of them goes to Home first.</p>
    <h2>Apps: three modes</h2>
    <dl>
      <dt>Filtered</dt><dd>The app works and trackers are stopped. Its lookups go through the firewall, so encryption, tracker blocking and your domain rules all apply. New apps start here, unless you choose Blocked in Settings under New apps.</dd>
      <dt>Not filtered</dt><dd>The firewall leaves the app alone. Untouched, costs nothing. Use it for an app that has trouble.</dd>
      <dt>Blocked</dt><dd>The app cannot go online. When it tries, you get a notice with an Allow button, at most once every 12 hours for each app. Turn the notice off in Settings under New apps.</dd>
    </dl>
    <p>Changes take effect at once, but an app that is already running can hold on to what it opened earlier, so close and reopen it. Change all sets every app in the list you are looking at, and Undo puts each one back. Apps that went online lately are at the top. Tap an app's row for its own page: what it looked up, which tracker companies it reached, and whether they got through.</p>
    <h2>Your domain rules</h2>
    <p>In Settings, under Protection. A block list and an allow list for ordinary websites, separate from the tracker lists. A rule covers the domain and everything under it, so blocking google.com also blocks www.google.com and mail.google.com. The more specific rule wins, so you can block a domain and allow one name inside it. Rules apply at once, for every app set to Filtered.</p>
    <p>Free: 3 rules, block and allow together. Pro: as many as you like, and wildcards. A star anywhere else, like <code>ads.*</code> or <code>*tracker*</code>, matches any text in its place.</p>
    <h2>Tracker lists</h2>
    <p>In Settings, under Protection. Every lookup is checked against known tracker, ad and fingerprinting domains. The bundled list works out of the box. With Pro you can add the community lists (HaGeZi, OISD, 1Hosts, Steven Black, AdGuard), refresh them, or add your own list by its https link: a hosts file, a plain list of domains, or an adblock style list. Lists are downloaded once and kept on the phone; the page shows how many names they hold and the memory they take. Anything a list gets wrong can be undone with an allow rule in Your domain rules.</p>
    <h2>Encrypted lookups (DNS over HTTPS)</h2>
    <p>In Settings, under Protection. Plain DNS shows your network every site you open. DNS over HTTPS encrypts the lookups. Google is free. With Pro you can pick Cloudflare, Quad9 or AdGuard, or type the address of any provider; Firewall tries a real lookup before it saves it. If the provider cannot be reached, Firewall falls back to the network's own resolver rather than leaving you with no answer.</p>
    <h2>Activity</h2>
    <p>Lookups seen, how many were stopped, what share were encrypted, and what did the stopping: a tracker list, your own rules, or a blocked app. The chart of the last 24 hours, the names blocked most often, and the full log, searchable, with the app behind every entry. Tap an entry to block that domain, or to always allow it. When the app itself was blocked, the entry offers to allow the app.</p>
    <p>Pro adds the chart of the last 7 days (30 days when you keep a longer history), your busiest hours of the day, the apps that look up the most, the tracker companies behind them, and Export CSV.</p>
    <h2>Alerts (Pro)</h2>
    <dl>
      <dt>New apps</dt><dd>Tells you when a newly installed app goes online, so you can allow or block it from the notification. With App Lock on, the notification only opens the app.</dd>
      <dt>New tracker companies</dt><dd>Tells you when an app reaches a tracker company it never reached before. An app the firewall has not seen before gets a day to show its usual companies quietly.</dd>
    </dl>
    <p>Turn them on in Settings, under Alerts and weekly summary.</p>
    <h2>Daily mobile data cap (Pro)</h2>
    <p>Open an app's page from the Apps tab and tap Daily mobile data cap. When the app has used that much mobile data today, its new connections are stopped on mobile data until midnight. Wi-Fi still works. Android counts the data, so Firewall needs Usage access; the app takes you to that screen. Caps need Android 10 or newer, and a cap cannot stop an app set to Not filtered.</p>
    <h2>History</h2>
    <p>The log is kept on your phone for 7 days. With Pro you can keep 30 or 90 days, in Settings under History. Longer history uses more storage.</p>
    <h2>Settings</h2>
    <p>Settings is the last button in the bar. It lists the pages below in groups: Look, Protection (Encrypted lookups, Tracker lists, Your domain rules, New apps), Lock, alerts and backup, Pro, and App (Privacy, Help and feedback), then Support the developer and About.</p>
    <dl>
      <dt>Look</dt><dd>Follow the phone, Light, Dark or Black. Black uses true black grounds, which save power on OLED screens.</dd>
      <dt>New apps</dt><dd>Whether a newly installed app starts Filtered or Blocked, and whether a blocked app that tries to go online brings a notice with Allow.</dd>
      <dt>App Lock</dt><dd>A passcode before the app opens, so your rules cannot be changed by someone holding your phone. Letters, digits and symbols are all allowed.</dd>
      <dt>Weekly summary (Pro)</dt><dd>Once a week, a notification with what the firewall stopped and which tracker companies your apps went for.</dd>
      <dt>Backup and restore</dt><dd>Saves how each app is handled, your domain rules, which tracker lists you downloaded, and your tracker and encryption settings, as plain JSON. Your passcode, your activity and your counters are never included. Restore here or on another phone.</dd>
      <dt>Privacy</dt><dd>Its own page. Firewall's promises (no ads, no tracking, no analytics, no account, no AI), then every permission it asks for and why. Location, contacts, camera and microphone are never asked for.</dd>
      <dt>Help and feedback</dt><dd>Its own page, with links to this guide and to the form to report a bug or ask for a feature.</dd>
      <dt>Support the developer</dt><dd>If Firewall helps you, you can support it: Buy me a coffee opens the page in your browser.</dd>
      <dt>About</dt><dd>The version you have, and that Firewall has no server of its own.</dd>
    </dl>
    <h2>Always on</h2>
    <p>Firewall starts again after a reboot and after an app update. The Quick Settings tile switches it from the notification shade, and respects App Lock. The Firewall status widget shows whether protection is on and what was stopped today.</p>
    <h2>Firewall Pro</h2>
    <p>One payment on Google Play, no subscription, no account. It stays with your Google account. If you used Firewall before Pro existed, Pro is already yours, for free.</p>
    </article>'''

FAQ = '''    <p class="kicker">Questions</p>
    <h1>Questions and fixes</h1>
    <article>
    <h2>An app or a site stopped working</h2>
    <p>Open Activity and look for its lookups marked as stopped. If the app itself is blocked, tap the entry and pick Allow, or tap Allow on the notice. Otherwise pick always allow for that name, or set the app to Filtered or Not filtered on the Apps tab. If a tracker list blocked a name the app needs, an allow rule in Settings, Your domain rules undoes it.</p>
    <h2>I blocked an app, but it still works</h2>
    <p>Close it and open it again: an app that was already running can hold on to what it opened earlier. An app that connects straight to an address, without looking up a name, cannot be stopped by a firewall that works on names.</p>
    <h2>It says Private DNS is in the way</h2>
    <p>With Private DNS set to a provider, Android sends every lookup straight there and the firewall never sees them. Tap the warning: Firewall can switch Private DNS to Automatic while it runs and put your setting back when you turn it off, or you can set it to Automatic or Off yourself under Network and internet. Turn on DNS over HTTPS in Firewall to keep lookups encrypted.</p>
    <h2>The firewall turned itself off</h2>
    <p>Android allows one VPN at a time. Starting another VPN app stops Firewall; switch it back on when you are done.</p>
    <h2>Does it drain the battery?</h2>
    <p>Very little. Only the names your phone looks up pass through the app, never your traffic itself.</p>
    <h2>The data cap shows no data used</h2>
    <p>Firewall needs Usage access to read Android's data counts. Open the app's page, tap the cap row and follow the button to Usage access, then turn Firewall on in that list. Caps count mobile data only.</p>
    <h2>I bought Pro on another phone</h2>
    <p>Sign in to Google Play with the same account and open Firewall. Pro comes back on its own.</p>
    <h2>Does Firewall send my data anywhere?</h2>
    <p>No. There is no account, no analytics and no server of ours. Lookups you allow go to the DNS provider you chose, as they would without the app. See the <a href="https://firewall.zanoski.com/privacy">privacy policy</a>.</p>
    </article>'''

REPORT = f'''    <p class="kicker">Report</p>
    <h1>Report a bug or ask for a feature</h1>
    <p>Found something broken, or have an idea? Tell us on GitHub. A free GitHub account is all you need.</p>
    <div class="grid">
      <div class="card"><h3>Bug report</h3><p>Something does not work, looks wrong or crashes.</p><p class="go"><a class="btn main" href="{REPO}/issues/new?template=bug_report.yml">Report a bug</a></p></div>
      <div class="card"><h3>Feature request</h3><p>Something you would like Firewall to do.</p><p class="go"><a class="btn" href="{REPO}/issues/new?template=feature_request.yml">Ask for a feature</a></p></div>
    </div>
    <article>
    <h2>Before you write</h2>
    <ul>
      <li>Search the <a href="{REPO}/issues">open issues</a> first. If yours is there, add a thumbs up or a comment.</li>
      <li>Check the <a href="faq.html">questions and fixes</a>.</li>
      <li>One problem per report makes it faster to fix.</li>
    </ul>
    <h2>What helps</h2>
    <dl>
      <dt>App version</dt><dd>Firewall, Settings, About, at the bottom.</dd>
      <dt>Phone model and Android version</dt><dd>Android settings, About phone.</dd>
      <dt>Which screen</dt><dd>Home, Apps, Activity, a Settings page such as Tracker lists or Your domain rules, an app's page, the tile, the widget or a notification.</dd>
      <dt>The app and the domain</dt><dd>Which app misbehaves and, from Activity, the name it looked up.</dd>
      <dt>Steps</dt><dd>What you did, one step per line.</dd>
    </dl>
    <p>Issues on GitHub are public. Your activity log shows which sites you visit, so crop screenshots and leave out anything private.</p>
    <h2>Other ways</h2>
    <p>Prefer not to use GitHub? Write to marko@zanoski.com (<a href="mailto:marko@zanoski.com">write an email</a>).</p>
    </article>'''

bad = 0
for (file, title), desc, body in zip(PAGES,
        ['The user guide for Firewall, the no root firewall for Android with tracker blocking and DNS over HTTPS.',
         'How to use Firewall: app modes, domain rules, tracker lists, encrypted lookups, activity, alerts, data caps and settings.',
         'Answers to common questions about Firewall.', 'How to report a Firewall bug or ask for a feature.'],
        [INDEX, GUIDE, FAQ, REPORT]):
    html = shell(file, title, desc, body)
    text = re.sub(r'<[^>]+>', ' ', html)
    for m in re.finditer(r'\s[-–—]\s|–|—', text):
        bad += 1; print(file, 'dash near', text[max(0, m.start() - 30):m.end() + 30].replace('\n', ' '))
    (ROOT / file).write_text(html)
    print('built', file)
sys.exit(1 if bad else 0)
