# Approach video

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
