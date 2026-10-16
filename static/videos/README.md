# Approach video

Place the final MP4 here as `dyad-approach.mp4`, then set the `data-video-src`
attribute on `#approach-video` in `index.html` to:

```html
data-video-src="static/videos/dyad-approach.mp4"
```

A hosted MP4 URL also works. No JavaScript changes are needed. The page uses
native playback controls and `playsinline`, with no autoplay. Until a video is
configured, visitors see the architecture figure and a "Video walkthrough coming
soon" label. A load error restores that fallback.

The poster is `static/images/dyad-architecture.png`. Replace it with a dedicated
video poster if desired. Add captions through a `<track kind="captions">` element
when the final video includes narration.
