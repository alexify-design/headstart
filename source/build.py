src=open('web/headstart.html').read()
head='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, maximum-scale=1, user-scalable=no">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="HeadStart">
<meta name="theme-color" content="#5B3DF5">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="icon" href="icon-192.png">
<link rel="manifest" href="manifest.json">
'''
native='''<style>
html,body{margin:0;overscroll-behavior:none;-webkit-user-select:none;user-select:none;-webkit-touch-callout:none;-webkit-text-size-adjust:100%}
input{-webkit-user-select:text;user-select:text;font-size:16px}
img{max-width:100%}[hidden]{display:none!important}
/* hide host badges that float over the tab bar */
[id*="netlify" i],[class*="netlify" i],a[href*="netlify.com"]{display:none!important}
/* safe areas + full-screen height are handled inside the app (--sat, --sab, --app-h) */
</style>
</head>
<body>
'''
src=src.replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
i=src.index('<div id="app">')
out=head+src[:i]+native+src[i:]+'\n</body>\n</html>\n'
out=out.replace('>Prototype</span>','>Beta</span>')
open('app/HeadStart/index.html','w').write(out)
s=out.split('<script>')[1].split('</script>')[0];open('check.js','w').write(s)
