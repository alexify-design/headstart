# HeadStart

**Starting is the hard part. We'll do it with you.**

HeadStart is a study app prototype for university students who know what they need to do but struggle to start. It turns assignments into small quests, puts them into real free evenings before the deadline, and runs a Pomodoro focus timer while distracting apps "nap".

Made for **ICD357 Design Research** · Group 3 · Project: *Losing Focus* · Instructor: Arjan Pupik

> Students don't struggle to study. They struggle to start.

## Try it

- Open `index.html` in a browser, or visit the GitHub Pages link (see below).
- On iPhone: open the link in **Safari → Share → Add to Home Screen** to use it like a native app.

## Two user journeys

| Persona | Signs in with | Journey |
|---|---|---|
| **Alex** | School account (Microsoft Teams) | Assignments import automatically → pick one → suggested steps, own steps, or just reminders → real-date plan → focus timer → final check → hand in |
| **Ploy** | Google | Adds assignments by typing → reminders go to Google Calendar → tiny starts → rescue mode near the deadline |

## Features

- Starts from zero: nothing planned, no streak, Level 1
- Real dates and times: deadlines, quest days, reminders and the timer use the device clock
- Pick a day and time for each of your own steps, or let the app choose a free evening
- Pomodoro focus timer with alarm pop-ups that continue by themselves after 10 seconds
- Streaks, XP, levels, stickers and buddy wardrobe that grow from real focus time
- Glass header on scroll, scroll-reveal cards, haptic taps (Android)
- Log out keeps your progress; sign back in to pick up where you left off
- Phone layout with bottom tabs, laptop layout with a sidebar, and a "Phone view" preview on laptops

## Files

| Path | What it is |
|---|---|
| `index.html` | The app (home-screen ready build) |
| `manifest.json`, `*.png` | App icon and install settings |
| `source/headstart.html` | Editable source |
| `source/build.py` | Builds `index.html` from the source |

## Publish with GitHub Pages

Settings → Pages → Source: **Deploy from a branch** → Branch: `main` / `(root)` → Save. The site appears at `https://<your-username>.github.io/<repo-name>/` after a minute.
