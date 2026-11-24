"""Builds the guide pages in docs/ from the bodies below, so they share one head, bar and footer, and refuses any
dash used as punctuation. python3 build.py"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).parent / 'docs'
PLAY = 'https://play.google.com/store/apps/details?id=com.zanoshky.firewall&amp;referrer=utm_source%3Dgithub_guide%26utm_medium%3Dreferral%26utm_campaign%3Dfirewall-2026-11'
SITE = 'https://firewall.zanoski.com'
REPO = 'https://github.com/Zanoshky/firewall-app'
PAGES = [('index.html', 'Home'), ('guide.html', 'Guide'), ('cookbook.html', 'Cookbook'), ('runbook.html', 'Runbook'), ('faq.html', 'Questions'), ('report.html', 'Report a bug')]

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
    <p class="sub">A firewall for Android that needs no root, with tracker blocking, DNS over HTTPS, and a log of everything your phone looks up. You decide, app by app, what the firewall does with it. Free, with an optional Pro and an optional Insider plan.</p>
    <div class="shots">
      {shot("apps", "The app list with lookups per app: Chrome, Calendar and Phosphor Filtered, Vinyl Blocked, and the bar at the bottom ending in Settings.", "Apps: Not filtered, Filtered or Blocked")}
      {shot("activity", "3.7K lookups, 1.0K blocked, 98% encrypted, and why lookups were stopped: tracker lists, your rules and blocked apps.", "Activity")}
      {shot("settings", "Settings: Look, then Protection with Encrypted lookups, Tracker lists, Your domain rules and New apps.", "Settings")}
      {shot("domains", "Your domain rules: a block list holding graph.facebook.com and tiktok.com, 2 of 3 free rules used.", "Your domain rules")}
      {shot("trackers", "Tracker lists: tracker blocking on with 129 names loaded, 848 blocked, and the memory the lists take.", "Tracker lists")}
    </div>
    <h2>New in 1.100</h2>
    <ul>
      <li>Kill switch: when another VPN app takes the VPN slot, your Blocked apps stay cut off and Firewall tells you with a notice and a line on Home.</li>
      <li>The widget and Self check no longer take the VPN slot from another VPN app. Firewall only takes the slot when you turn it on.</li>
      <li>Another VPN app knocks Firewall off? Android lets any VPN app you once allowed take the slot without asking. In Android Settings, VPN, turn on Always on VPN for the one you want to keep.</li>
    </ul>
    <h2>New in 1.98</h2>
    <ul>
      <li>Self check, in Settings under Help: Firewall looks at its own setup and says in plain words what could stop it from working. In No VPN mode it says which parts of Firewall that mode does not use.</li>
      <li>The widget draws a ring of how many of today's lookups were stopped, is four cells wide, and the Quick Settings tile says Protected, Watch only, Not filtering or Off under its name. Settings has an Add to Quick Settings row.</li>
      <li>A downloaded tracker list that is two weeks old or more now says it is older than it should be.</li>
      <li>Automation can turn the firewall on again from Tasker.</li>
    </ul>
    <h2>New in 1.91</h2>
    <ul>
      <li>A Setup guide in Settings that checks each step on the phone as you read, and a Pro tour that does the same for the Pro features.</li>
      <li>Pro: the DNS Inspector, DNS guard, DNS through Tor with its own setup page, and a weekly refresh of your downloaded lists.</li>
      <li>Insider: Insights joins No VPN mode, Open doors and Automation.</li>
      <li>Activity shows a privacy score, charts and the countries your apps reach.</li>
      <li>You can block one domain for one app only, and add the widget from Settings.</li>
      <li>Safer: a blocked app cannot reuse a name, payments are checked again, and Tor lookups refuse a port held by an app that is not Orbot or Tor Browser.</li>
    </ul>
    <h2>New in 1.77</h2>
    <ul>
      <li>No VPN mode moved from Pro to Insider too (1.78). Pro owners no longer have it; if Insider ends while it is on, No VPN mode and the firewall switch off, and you turn the firewall on again from Home.</li>
      <li>Automation and Open doors moved from Pro to Insider. Pro owners no longer have them; Insider now gives Automation, Open doors, No VPN mode, new features first, an Insider mark in About and your requests read first.</li>
    </ul>
    <h2>New in 1.55</h2>
    <ul>
      <li>Insider, the optional monthly plan, brings new features first, reads your reports first and adds a mark in About (since 1.77 it also gives Automation and Open doors, and since 1.78 No VPN mode).</li>
      <li>Firewall says when it is not filtering: Home, the notification and the widget read Not filtering while Private DNS sends lookups past it, and a notice tells you when Android stopped it.</li>
      <li>Domain rules take names in any script, and every place that adds a rule counts toward the 3 free ones.</li>
      <li>Another app, such as Netglow, our network scanner, can ask Firewall to block an app. Firewall asks you first.</li>
      <li>Block lists use far less memory, long DNS answers work again, and Greek, Cyrillic, Vietnamese and more letters show in the app's own fonts.</li>
    </ul>
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
    <h2>Setup guide</h2>
    <p>In Settings, open Setup guide. It lists Turn Firewall on, Pick how strict, encrypted lookups, tracker lists and Keep it running, and checks each one on the phone as you read. Nothing is a saved tick, so it stays true after a restart. Tap a step to do it. Come back after a restart or a crash and the page checks again and says what changed. If this phone has its own battery setting that Android cannot read, the page asks you to open it, choose No restrictions and tap I set it.</p>
    <h2>Apps: three modes</h2>
    <dl>
      <dt>Filtered</dt><dd>The app works and trackers are stopped. Its lookups go through the firewall, so encryption, tracker blocking and your domain rules all apply. New apps start here, unless you choose Blocked in Settings under New apps.</dd>
      <dt>Not filtered</dt><dd>The firewall leaves the app alone. Untouched, costs nothing. Use it for an app that has trouble.</dd>
      <dt>Blocked</dt><dd>The app cannot go online. When it tries, you get a notice with an Allow button, at most once every 12 hours for each app. Turn the notice off in Settings under New apps.</dd>
    </dl>
    <p>Changes take effect at once, but an app that is already running can hold on to what it opened earlier, so close and reopen it. Change all sets every app in the list you are looking at, and Undo puts each one back. Apps that went online lately are at the top. Tap an app's row for its own page: what it looked up, which tracker companies it reached, and whether they got through.</p>
    <h2>Your domain rules</h2>
    <p>In Settings, under Protection. A block list and an allow list for ordinary websites, separate from the tracker lists. A rule covers the domain and everything under it, so blocking google.com also blocks www.google.com and mail.google.com. The more specific rule wins, so you can block a domain and allow one name inside it. Rules apply at once, for every app set to Filtered. Names in any script work, like bücher.de; a name can be up to 253 characters.</p>
    <p>Free: 3 rules, block and allow together, whether you add them here, from Activity or from an app's page. Pro: as many as you like, and wildcards. A star anywhere else, like <code>ads.*</code> or <code>*tracker*</code>, matches any text in its place.</p>
    <h2>Tracker lists</h2>
    <p>In Settings, under Protection. Every lookup is checked against known tracker, ad and fingerprinting domains. The bundled list works out of the box. With Pro you can add the community lists (HaGeZi, OISD, 1Hosts, Steven Black, AdGuard), refresh them, or add your own list by its https link: a hosts file, a plain list of domains, or an adblock style list. Lists are downloaded once and kept on the phone; the page shows how many names they hold and the memory they take. Refresh weekly, on by default, downloads your lists again once a week on unmetered Wi-Fi only, and any failure keeps the copy you have. Anything a list gets wrong can be undone with an allow rule in Your domain rules.</p>
    <h2>Encrypted lookups (DNS over HTTPS)</h2>
    <p>In Settings, under Protection. Plain DNS shows your network every site you open. DNS over HTTPS encrypts the lookups. Google is free. With Pro you can pick Cloudflare, Quad9 or AdGuard, or type the address of any provider; Firewall tries a real lookup before it saves it. If the provider cannot be reached, Firewall falls back to the network's own resolver rather than leaving you with no answer.</p>
    <h2>Forced SafeSearch</h2>
    <p>In Settings, under Encrypted lookups. Google, Bing and DuckDuckGo always show their SafeSearch results, and YouTube runs in Restricted Mode, in every app the firewall filters. A browser with its own Secure DNS turned on asks its own server and gets past this, so turn that off in the browser too. Free.</p>
    <h2>Activity</h2>
    <p>Lookups seen, how many were stopped, what share were encrypted, and what did the stopping: a tracker list, your own rules, or a blocked app. The chart of the last 24 hours, the names blocked most often, and the full log, searchable, with the app behind every entry. Tap an entry to block that domain, or to always allow it. When the app itself was blocked, the entry offers to allow the app.</p>
    <p>The top of Activity shows a privacy score with a grade, and how many lookups were stopped.</p>
    <p>Pro adds the chart of the last 7 days (30 days when you keep a longer history), your busiest hours of the day, the apps that look up the most, the tracker companies behind them, Countries contacted (where the answers to your apps' lookups pointed in the last 7 days, from a table kept on the phone), the most contacted addresses, and Export CSV.</p>
    <h2>Alerts (Pro)</h2>
    <dl>
      <dt>New apps</dt><dd>Tells you when a newly installed app goes online, so you can allow or block it from the notification. With App Lock on, the notification only opens the app.</dd>
      <dt>New tracker companies</dt><dd>Tells you when an app reaches a tracker company it never reached before. An app the firewall has not seen before gets a day to show its usual companies quietly.</dd>
    </dl>
    <p>Turn them on in Settings, under Alerts and weekly summary.</p>
    <h2>Daily mobile data cap (Pro)</h2>
    <p>Open an app's page from the Apps tab and tap Daily mobile data cap. When the app has used that much mobile data today, its new connections are stopped on mobile data until midnight. Wi-Fi still works. Android counts the data, so Firewall needs Usage access; the app takes you to that screen. Caps need Android 10 or newer, and a cap cannot stop an app set to Not filtered.</p>
    <h2>DNS Inspector (Pro)</h2>
    <p>In Settings, open DNS Inspector. It shows every lookup as a packet, as in Wireshark: who asked, what for, the answer and the raw bytes. Turn on Capture lookups to keep the last 500 lookups in memory. They are never saved. Export as pcapng opens in Wireshark with the app named in each packet. Live link for Wireshark streams packets over adb, and no other app can connect. Tap a lookup to copy it as a dig command, a DoH curl command, a Wireshark filter or just the domain. Test lookup asks the system and every resolver the same question, and tells you when one returns no addresses or a private address, which can be a local override or a hijack.</p>
    <h2>DNS rules and DNS guard (Pro)</h2>
    <p>In Settings, open DNS rules. Use the network's DNS for local names keeps names like printer.local or router.lan, and Wi-Fi login pages, working. With Pro, Block DNS tunnelling refuses very long names and names that look like encoded data, and you can refuse record types such as ANY, TXT, NULL and HTTPS. Refused lookups show in Activity as blocked.</p>
    <h2>Kill switch (Pro)</h2>
    <p>In Settings, under Protection. Normally Firewall stops a Blocked app by refusing every name it looks up. A few apps get past that by connecting straight to an address. With the Kill switch on, Android itself cuts a Blocked app off, so it cannot reach the internet at all, and a connection it already had stops at once. Filtered and Not filtered apps are not touched, and it costs no battery.</p>
    <p>It needs Android 13 or newer and Shizuku, a free helper app. Android only lets its own system tools switch another app's internet off; Shizuku lends Firewall that one power without rooting the phone. Turn the switch on and the page shows one step at a time: get Shizuku, start it, allow Firewall. After a phone restart, open Shizuku and tap Start once; Firewall reminds you. Until then Blocked works the normal way.</p>
    <p>Turning the Kill switch or the firewall off gives every app its connection back. A few parts of the phone are never cut off this way: Firewall and Shizuku, the network stack, calls, Settings, the launcher and Google Play services. An app that came with the phone is only cut off if you blocked it yourself. Shizuku also lets Firewall handle strict Private DNS without the adb command.</p>
    <h2>No VPN mode (Insider)</h2>
    <p>In Settings, under Protection, open Protection mode and pick Normal, Watch only or No VPN. In No VPN mode Firewall never starts its VPN, so your VPN slot stays free for another VPN app. Shizuku and Android's own firewall cut the apps you Blocked, the same way the Kill switch does, and the Kill switch turns on with it.</p>
    <p>Self check in this mode says so plainly: tracker lists, encrypted lookups and Private DNS are not used, and it sends no test lookup. Be clear about the trade: only whole apps can be cut. There is no name filtering, no tracker blocking, no domain rules and no Activity log, and Watch only, Screen off and DNS guard pause. The page shows one step at a time to get Shizuku running, and asks you to confirm before it starts.</p>
    <p>After a phone restart nothing is blocked until you open Shizuku and tap Start again; Firewall shows "No VPN mode paused" with a Fix button and posts a reminder, and the cut comes back on its own once Shizuku runs. Switch back to Normal at any time and the VPN returns.</p>
    <h2>DNS through Tor (Pro)</h2>
    <p>Your encrypted lookups normally go to the provider you picked, and it sees which phone asks. With DNS through Tor they travel through Orbot, the free Tor app, so the provider sees Tor and not you. It hides who is asking from your DNS provider and your network. It does not hide the connections your apps make themselves. The first lookups can take a few seconds while Tor builds a circuit.</p>
    <p>Set it up once, in this order. The Pro tour in Settings shows each step and ticks it only when your phone proves it.</p>
    <ol>
      <li>Install Orbot from Google Play (F-Droid has it too).</li>
      <li>Open Orbot, then its Settings, General, and turn on Power User Mode. This matters: without it Orbot takes over the phone's one VPN slot and Firewall stops.</li>
      <li>In the same General settings, turn on Start Orbot on Boot, so it comes back after a restart.</li>
      <li>On the Orbot start screen leave the transport on Direct Connection (or Smart Connect), tap Connect and wait for Connected.</li>
      <li>In Firewall, make sure Encrypted lookups is on, then open Settings, DNS rules and turn on Send encrypted lookups through Tor.</li>
    </ol>
    <p>Refuse lookups if Tor is down decides what happens when Orbot stops. On, no lookup is answered until Orbot is back, so nothing leaks to your provider. Off, Firewall falls back to the normal encrypted path. Check Orbot on the same page tells you if Tor is reachable. If Orbot is not running, the Pro tour shows an amber mark with what to do. Also set Orbot's battery to Unrestricted in Android settings, so Android does not stop it. Firewall asks Android which app holds the Tor port, and refuses to send lookups to one that is not Orbot or Tor Browser.</p>
    <h2>Wi-Fi, mobile data and roaming</h2>
    <p>Open an app from the Apps list. Under Can connect on there are three tiles: Wi-Fi, Mobile data and Roaming. Tap one to block or allow the app on that network. An app blocked on mobile data shows Wi-Fi only on the Apps list. Roaming counts as mobile data too, so an app blocked on mobile data is also blocked while roaming. The rule works for Filtered and Not filtered apps alike. Free.</p>
    <h2>Data used</h2>
    <p>Firewall can show how much data each app used, the same count Android keeps in its own data usage settings. It needs Usage access, which you allow from the app sheet with Allow usage access (Android 10 or newer). Then the Apps list shows each app's data today and can sort by Most data, and the app sheet shows Today, 7 days and 30 days: downloaded, uploaded, Wi-Fi against mobile data, and a chart of the day. Change all now sits in the sort menu. Free.</p>
    <h2>Screen off</h2>
    <p>In Settings, under Protection. With Block while the screen is off on, apps cannot go online while you are not using the phone. It starts 1 minute after the screen goes off, so a quick look at the clock changes nothing, and stops the moment the screen comes on. The apps under Stay online keep working: your phone app, your messages app and Google Play services, which carries notifications for every app. Add music or a messenger with Add an app. Free.</p>
    <h2>History</h2>
    <p>The log is kept on your phone for 7 days. With Pro you can keep 30 or 90 days, in Settings under History. Longer history uses more storage.</p>
    <h2>Automation (Insider)</h2>
    <p>In Settings, under Automation. It lets Tasker, MacroDroid or a shell script set one app's mode, for example Blocked while you are at work. Turn on Allow automation and Firewall shows a secret token; every request must carry it, and a request with the wrong token is ignored. Copy token and Copy the example with your token give you a ready command to paste into your automation app, and Make a new token stops the old one at once. The page also shows the last request and what became of it.</p>
    <p>A request can only set an app's mode (Blocked, Filtered or Not filtered). It cannot read your log, change your rules or turn the firewall off. Automation is part of Insider; it was part of Pro until 1.77, so Pro alone no longer unlocks it.</p>
    <h2>Open doors (Insider)</h2>
    <p>In Settings, under Open doors. It shows which apps on this phone take connections from your Wi-Fi, and who each app talks to right now. It reads Android's socket tables through Shizuku, a free helper app, and looks again every 2 seconds while the page is open. Nothing leaves the phone and no name is looked up.</p>
    <p>Listening on your Wi-Fi lists the open ports another device on the same Wi-Fi can try to connect to; risky ones, such as Android debugging, Telnet, FTP, file sharing, screen sharing, a remote login, a proxy or a database, are marked red with a line saying why. Talking right now lists live connections as numbers. Open doors is part of Insider; it was part of Pro until 1.77, so Pro alone no longer unlocks it.</p>
    <h2>Insights (Insider)</h2>
    <p>In Settings, open Insights. It shows what your log says about the last 7, 30 or 90 days, up to the history you keep: which apps talk most and their tracker share, the names stopped most often, the tracker companies, activity at night, a week by hour map, the trend against the period before, data per app (this needs Usage access), names seen for the first time, reasons and protocol mix, how fast answers come each day, and streaks. You can export it as CSV. All of it is worked out on this phone from the log, and nothing leaves it.</p>
    <h2>Settings</h2>
    <p>Settings is the last button in the bar. It lists the pages below in groups: Look, Protection (Encrypted lookups, Tracker lists, Your domain rules, New apps, Screen off, Kill switch), Lock, alerts and backup, Pro, and App (Privacy, Help and feedback), then Support the developer and About.</p>
    <dl>
      <dt>Look</dt><dd>Follow the phone, Light, Dark or Black. Black uses true black grounds, which save power on OLED screens.</dd>
      <dt>New apps</dt><dd>Whether a newly installed app starts Filtered or Blocked, and whether a blocked app that tries to go online brings a notice with Allow.</dd>
      <dt>App Lock</dt><dd>A passcode before the app opens, so your rules cannot be changed by someone holding your phone. Letters, digits and symbols are all allowed.</dd>
      <dt>Weekly summary (Pro)</dt><dd>Once a week, a notification with what the firewall stopped and which tracker companies your apps went for.</dd>
      <dt>Backup and restore</dt><dd>Saves how each app is handled, your domain rules, which tracker lists you downloaded, and your tracker and encryption settings, as plain JSON. Your passcode, your activity and your counters are never included. Restore here or on another phone.</dd>
      <dt>Privacy</dt><dd>Its own page. Firewall's promises (no ads, no tracking, no analytics, no account, no AI), then every permission it asks for and why. Location, contacts, camera and microphone are never asked for.</dd>
      <dt>Add to Quick Settings</dt><dd>Android asks you to confirm, then the Firewall tile turns the firewall on or off from the swipe down panel and says its state under its name. Before Android 13 the page shows the manual way: swipe down twice, tap the pencil and drag Firewall into your tiles.</dd>
      <dt>Add the widget</dt><dd>Pins the Firewall status widget to your home screen. It draws a ring of how many of today's lookups were stopped, with the count inside, and one key to turn the firewall on or off. If your launcher cannot add it from here, touch and hold an empty spot on the home screen, tap Widgets, then pick Firewall.</dd>
      <dt>Self check</dt><dd>Under Help. One row for each thing that could stop Firewall from working: whether it runs (or Watch only, or No VPN mode), the VPN permission, another VPN holding the slot, notifications, battery saving, the tracker lists (and how old the newest downloaded one is), encrypted lookups, Private DNS and the Kill switch. Each row has a tick, a ban sign or an info sign. The only thing it sends out is one test lookup of example.com to your own DNS over HTTPS provider, and only when encrypted lookups are on and Tor is not carrying them. Copy result puts the rows on the clipboard for a support mail. It holds no domain, no app name and no address that was looked up.</dd>
      <dt>Help and feedback</dt><dd>Its own page, with links to this guide and to the form to report a bug or ask for a feature.</dd>
      <dt>Support the developer</dt><dd>If Firewall helps you, you can support it. Insider is an optional subscription, 0.99 a month through Google Play, that pays for bug fixes and fresh tracker lists. Insiders get Automation, Open doors, No VPN mode and Insights, new features before everyone else (each one opens to every user on a set date), their bug reports and ideas read first, and an Insider mark in About with their date. Automation and Open doors used to be part of Pro and moved to Insider in 1.77, and No VPN mode followed in 1.78; apart from those three, nothing free or in Pro moves behind it. Once you subscribe, the row says thank you and opens Google Play, where you cancel any time.</dd>
      <dt>About</dt><dd>The version you have, and that Firewall has no server of its own.</dd>
    </dl>
    <h2>Always on</h2>
    <p>Firewall starts again after a reboot and after an app update. The Quick Settings tile switches it from the notification shade, and respects App Lock. The Firewall status widget shows whether protection is on and what was stopped today.</p>
    <p>Firewall never claims to protect you when it does not. While Private DNS sends lookups straight to its provider, Home, the notification and the widget say Not filtering; tap to fix it. If Android stops the firewall and it cannot come back, the switch goes off and a Firewall stopped notice asks you to turn it on again.</p>
    <h2>Requests from other apps</h2>
    <p>Netglow, our network scanner, runs no VPN of its own, so it asks Firewall. Any app may ask Firewall to block an app, but Firewall shows its own dialog first and nothing changes until you say yes. A request can only block, never let an app out again; change it back under Apps. While the firewall runs, Netglow can read the connection log, read only. No other app can, and Firewall checks Netglow by its name and its Google Play signature.</p>
    <h2>Languages and big screens</h2>
    <p>Firewall speaks English, German, Spanish, French, Hindi, Indonesian, Japanese, Korean, Brazilian Portuguese, Russian and Turkish. It follows the phone, or pick a language for Firewall alone in Android's settings, Apps, Firewall, Language. Greek, Cyrillic, Vietnamese and other accented letters show in the app's own fonts. It uses two columns on a tablet.</p>
    <h2>Firewall Pro</h2>
    <p>One payment on Google Play, no subscription, no account. It stays with your Google account. If you used Firewall before Pro existed, Pro is already yours, for free.</p>
    </article>'''

FAQ = '''    <p class="kicker">Questions</p>
    <h1>Questions and fixes</h1>
    <article>
    <h2>An app or a site stopped working</h2>
    <p>Open Activity and look for its lookups marked as stopped. If the app itself is blocked, tap the entry and pick Allow, or tap Allow on the notice. Otherwise pick always allow for that name, or set the app to Filtered or Not filtered on the Apps tab. If a tracker list blocked a name the app needs, an allow rule in Settings, Your domain rules undoes it.</p>
    <h2>I blocked an app, but it still works</h2>
    <p>Close it and open it again: an app that was already running can hold on to what it opened earlier. An app that connects straight to an address, without looking up a name, cannot be stopped by a firewall that works on names. With Pro, the Kill switch stops those too (Android 13 or newer, with Shizuku).</p>
    <h2>It says Private DNS is in the way</h2>
    <p>With Private DNS set to a provider, Android sends every lookup straight there and the firewall never sees them. Tap the warning: Firewall can switch Private DNS to Automatic while it runs and put your setting back when you turn it off, or you can set it to Automatic or Off yourself under Network and internet. Turn on DNS over HTTPS in Firewall to keep lookups encrypted.</p>
    <h2>The firewall turned itself off</h2>
    <p>Android allows one VPN at a time. Starting another VPN app stops Firewall; switch it back on when you are done. If Android stopped it, a Firewall stopped notice says so; tap it to turn the firewall back on.</p>
    <h2>Home says Not filtering</h2>
    <p>Private DNS is set to a provider, so lookups go past the firewall. Tap the warning and let Firewall move Private DNS aside while it runs.</p>
    <h2>I am uninstalling Firewall</h2>
    <p>Turn the firewall off first, so it puts your Private DNS setting back. If you uninstall it while it runs, set Private DNS back yourself under Network and internet.</p>
    <h2>Another app asked me to block an app</h2>
    <p>Apps like Netglow can ask Firewall to block an app. Firewall asks you in its own dialog, and a request can never unblock anything. Say no and nothing changes.</p>
    <h2>Does it drain the battery?</h2>
    <p>Very little. Only the names your phone looks up pass through the app, never your traffic itself.</p>
    <h2>The data cap shows no data used</h2>
    <p>Firewall needs Usage access to read Android's data counts. Open the app's page, tap the cap row and follow the button to Usage access, then turn Firewall on in that list. Caps count mobile data only.</p>
    <h2>I bought Pro on another phone</h2>
    <p>Sign in to Google Play with the same account and open Firewall. Pro comes back on its own.</p>

    <h2>What is Insider?</h2>
    <p>An optional subscription, 0.99 USD or EUR a month, for those who want to help more. It pays for bug fixes and fresh tracker lists. Insiders get Automation, Open doors and No VPN mode, new features before everyone else (each one opens to every user on a set date), their bug reports and ideas read first, and an Insider mark in About with their date. Automation and Open doors used to be part of Pro and moved to Insider in 1.77, and No VPN mode followed in 1.78; apart from those three, nothing free or in Pro moves behind it. Find it in Settings, under Support the developer. Cancel any time in Google Play.</p>
    <h2>Does Firewall send my data anywhere?</h2>
    <p>No. There is no account, no analytics and no server of ours. Lookups you allow go to the DNS provider you chose, as they would without the app. See the <a href="https://firewall.zanoski.com/privacy">privacy policy</a>.</p>
    </article>'''

COOKBOOK = '''    <p class="kicker">Cookbook</p>
    <h1>Short recipes</h1>
    <p>A few taps each. Every recipe starts from the bar at the bottom: Home, Apps, Activity and Settings.</p>
    <article>
    <h2>Stop trackers, keep the app working</h2>
    <ol><li>Open Apps and tap the app.</li><li>Pick Filtered.</li><li>Close the app and open it again.</li></ol>
    <p>It works as before, and Activity shows each tracker it tried to reach.</p>
    <h2>Keep an app off mobile data</h2>
    <ol><li>Open Apps and tap the app.</li><li>Under Can connect on, tap Mobile data to block it there.</li></ol>
    <p>The list then says Wi-Fi only for that app. Roaming counts as mobile data too.</p>
    <h2>Block a site in every app</h2>
    <ol><li>Open Settings, Your domain rules.</li><li>Add the domain to the block list, like example.com.</li></ol>
    <p>It covers www.example.com and every other name under it, for every app set to Filtered.</p>
    <h2>Safe search for a child's phone</h2>
    <ol><li>Open Settings, Encrypted lookups.</li><li>Turn on Forced SafeSearch.</li><li>In the browser, turn off its own Secure DNS.</li><li>Turn on App Lock in Settings, so nobody changes it.</li></ol>
    <h2>Quiet nights</h2>
    <ol><li>Open Settings, Screen off.</li><li>Turn on Block while the screen is off.</li><li>Under Stay online, add the apps you want to hear from, like your messenger.</li></ol>
    <p>It starts a minute after the screen goes off, and calls, messages and Google Play services keep working.</p>
    <h2>A daily mobile data cap (Pro)</h2>
    <ol><li>Open Apps and tap the app.</li><li>Tap Daily mobile data cap and pick an amount.</li><li>Allow Usage access when Firewall asks.</li></ol>
    <h2>Cut an app off completely (Pro)</h2>
    <ol><li>Set the app to Blocked.</li><li>Open Settings, Kill switch, and follow the steps: get Shizuku, start it, allow Firewall.</li></ol>
    <p>Needs Android 13 or newer. After a restart, open Shizuku and tap Start once.</p>
    <h2>Send lookups through Tor (Pro)</h2>
    <ol><li>Install Orbot, open its Settings, General and turn on Power User Mode and Start Orbot on Boot.</li><li>Tap Connect in Orbot and wait for Connected.</li><li>In Firewall, turn on Encrypted lookups, then Settings, DNS rules, Send encrypted lookups through Tor.</li></ol>
    <p>The Pro tour in Settings checks every step for you.</p>
    <h2>Your rules on a new phone</h2>
    <ol><li>On the old phone, Settings, Backup and restore, save a backup.</li><li>Copy the file to the new phone.</li><li>On the new phone, Backup and restore, Restore from file.</li></ol>
    <p>Your passcode and your activity are never in the backup.</p>
    <h2>Support Firewall monthly</h2>
    <ol><li>Open Settings and scroll to Support the developer.</li><li>Tap Insider.</li><li>Google Play shows the price and how to cancel. Confirm there.</li></ol>
    <p>Optional. Insiders get Automation, Open doors and No VPN mode, new features first and their requests read first. Tap the row again to manage or cancel it.</p>
    </article>'''

RUNBOOK = '''    <p class="kicker">Runbook</p>
    <h1>When something goes wrong</h1>
    <p>What you see, why it happens, and the taps that fix it. More answers are in the <a href="faq.html">questions</a>.</p>
    <article>
    <h2>An app or a site stopped working</h2>
    <p>Something it needs was stopped: the app itself, a tracker list, or one of your rules.</p>
    <ol><li>Open Activity and find its lookups marked as stopped.</li><li>Tap one and pick Always allow, or Allow for a blocked app.</li><li>Still broken? Set the app to Not filtered on the Apps tab, then close and reopen it.</li></ol>
    <h2>Firewall turned itself off</h2>
    <p>Android allows one VPN at a time, so another VPN app stops Firewall. Some phones also stop apps in the background to save battery.</p>
    <ol><li>Switch it back on from Home or the Quick Settings tile.</li><li>Android settings, Apps, Firewall, Battery: pick Unrestricted.</li><li>Network and internet, VPN, Firewall: turn on Always on VPN.</li></ol>
    <h2>Nothing shows in Activity, or Home says Not filtering</h2>
    <p>With Private DNS set to a provider, Android sends lookups straight there and Firewall never sees them.</p>
    <ol><li>Tap the Private DNS warning on Home.</li><li>Let Firewall switch it to Automatic while it runs, or set it yourself under Network and internet.</li></ol>
    <h2>A blocked app still gets online</h2>
    <p>It was already connected, or it connects straight to an address without a lookup.</p>
    <ol><li>Close the app and open it again.</li><li>With Pro, turn on the Kill switch (Android 13 or newer, with Shizuku).</li></ol>
    <h2>The Kill switch stopped after a restart</h2>
    <p>Shizuku has to be started again after every restart; Firewall reminds you.</p>
    <ol><li>Open Shizuku and tap Start.</li></ol>
    <p>Until then, Blocked works the normal way.</p>
    <h2>The Tor row says Orbot is not running</h2>
    <p>Orbot stops when the phone restarts, unless Start Orbot on Boot is on. While Refuse lookups if Tor is down is on, no name is answered until it is back.</p>
    <ol><li>Open Orbot and tap Connect, then wait for Connected.</li><li>In Orbot, Settings, General: turn on Power User Mode and Start Orbot on Boot.</li><li>If Firewall stops when Orbot connects, Power User Mode is off: Orbot is using the VPN slot.</li></ol>
    <h2>Data used or a cap shows nothing</h2>
    <p>Firewall reads Android's own data counts, which need Usage access.</p>
    <ol><li>Open the app's page and tap Allow usage access.</li><li>Turn Firewall on in Android's list.</li></ol>
    <h2>A tracker list will not download</h2>
    <p>The list's server is slow or gone, or the phone is short on memory for very big lists.</p>
    <ol><li>Open Settings, Tracker lists, and tap Refresh on that list.</li><li>Still failing? Remove one of the biggest lists; the page shows the memory each takes.</li></ol>
    <h2>Forgot the App Lock passcode</h2>
    <p>The passcode is kept only on the phone, and nobody, us included, can read it.</p>
    <ol><li>Android settings, Apps, Firewall, Storage, Clear storage.</li><li>Open Firewall and restore your last backup.</li></ol>
    <h2>Pro is missing on a new phone</h2>
    <ol><li>Sign in to Google Play with the account that bought it.</li><li>Open Firewall. Pro comes back on its own.</li></ol>
    <h2>The subscription will not start</h2>
    <p>Insider runs through the Google Play app. A copy not installed from Google Play, an old Play Store, or no account on the phone cannot reach it.</p>
    <ol><li>Open the Play Store once and check you are signed in.</li><li>Update Firewall and the Play Store.</li><li>Try the row again in Settings, under Support the developer.</li></ol>
    <p>To cancel: tap the same row, or Play Store, your profile, Payments and subscriptions.</p>
    </article>'''

REPORT = f'''    <p class="kicker">Report</p>
    <h1>Report a bug or ask for a feature</h1>
    <p>Found something broken, or have an idea? Tell us on GitHub. A free GitHub account is all you need.</p>
    <div class="grid">
      <div class="card"><h3>Bug report</h3><p>Something does not work, looks wrong or crashes.</p><p class="go"><a class="btn main" href="{REPO}/issues/new?template=bug_report.yml">Report a bug</a></p></div>
      <div class="card"><h3>Feature request</h3><p>Something you would like Firewall to do.</p><p class="go"><a class="btn" href="{REPO}/issues/new?template=feature_request.yml">Ask for a feature</a></p></div>
    </div>
    <p id="insider" hidden><b>Insider:</b> your request is read first. The title starts with [insider] so it stands out.</p>
    <script>
    document.addEventListener('DOMContentLoaded',function(){{if(!/[?&]insider=1(&|$)/.test(location.search))return;
    var n=document.getElementById('insider');if(n)n.hidden=false;
    document.querySelectorAll('a[href*="/issues/new"]').forEach(function(a){{var t=/feature_request/.test(a.href)?'[insider] [idea] ':'[insider] [bug] ';a.href+='&title='+encodeURIComponent(t)}});
    document.querySelectorAll('a[href^="mailto:"]').forEach(function(a){{a.href+=(a.href.indexOf('?')<0?'?':'&')+'subject='+encodeURIComponent('Insider: ')}})}});
    </script>
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
    <p>Prefer not to use GitHub? Write to support@zanoski.com (<a href="mailto:support@zanoski.com">write an email</a>).</p>
    </article>'''

bad = 0
for (file, title), desc, body in zip(PAGES,
        ['The user guide for Firewall, the no root firewall for Android with tracker blocking and DNS over HTTPS.',
         'How to use Firewall: app modes, domain rules, tracker lists, encrypted lookups, activity, alerts, data caps and settings.',
         'Short Firewall recipes: stop trackers, keep an app off mobile data, safe search, quiet nights, data caps and more.',
         'When something in Firewall goes wrong: a broken app, the VPN turning off, an empty Activity, the Kill switch, Pro and the subscription.',
         'Answers to common questions about Firewall.', 'How to report a Firewall bug or ask for a feature.'],
        [INDEX, GUIDE, COOKBOOK, RUNBOOK, FAQ, REPORT]):
    html = shell(file, title, desc, body)
    text = re.sub(r'<[^>]+>', ' ', html)
    for m in re.finditer(r'\s[-–—]\s|–|—', text):
        bad += 1; print(file, 'dash near', text[max(0, m.start() - 30):m.end() + 30].replace('\n', ' '))
    (ROOT / file).write_text(html)
    print('built', file)
sys.exit(1 if bad else 0)
