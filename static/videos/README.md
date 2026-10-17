# Project videos

## Overview

`dyad-overview.mp4` is the author-supplied overview animation added on
2026-10-17. It appears after the TL;DR and opening paragraph, before the first
numbered results section, under the small label **Dyad in one minute**.

The original H.264 and AAC streams are copied without re-encoding. The MP4 is
prepared for progressive playback with `faststart`, retaining the 1280 × 720
resolution and approximately 62.37-second duration. Its poster,
`static/images/dyad-overview-poster.jpg`, is taken at 60.5 seconds, before the
closing logo and slogan fade out.

The player is paused and muted by default, uses native controls, supports
inline mobile playback and has no autoplay or loop. The audio track is retained
and can be unmuted. JavaScript adds the overlay play button; the native controls
remain usable without it. A playback error exposes a direct MP4 link.

Replace the MP4, its poster, and the corresponding dimensions in `index.html`
when updating this video. Version the source and poster URLs if replacing their
contents at the same paths. Keep this overview separate from the detailed
architecture walkthrough below.

## Approach

`dyad-approach.mp4` is the author-supplied architecture animation, taken from the
2026-10-16 screen recording. It is connected to Figure 4 through the
`data-video-src` attribute on `#approach-video` in `index.html`:

```html
data-video-src="static/videos/dyad-approach.mp4?v=hold-ends-1s"
```

The MP4 contains a single H.264 video track and no audio tracks. All encoded
video packets are retained without re-encoding. The first and last frames each
hold for one additional second; all intermediate frame intervals retain their
original timing. The playable duration is about 31.3 seconds, at 2518 × 1166.
The MP4 places its metadata before the media data (`faststart`) for progressive
loading.

The page uses native playback controls, `muted`, and `playsinline`, with no
autoplay. Its poster, `static/images/dyad-approach-poster.jpg`, is taken from the
animation at 17 seconds. A load error restores the original architecture image;
the static fallback also remains available when JavaScript is disabled.

To replace the animation, overwrite the MP4 and update its poster and the
video's `width` / `height` attributes, and refresh the video URL's version query
when its contents change. A hosted MP4 URL also works in `data-video-src`;
no JavaScript changes are needed. Keep the export free of
audio tracks unless narration is intentionally added later.
