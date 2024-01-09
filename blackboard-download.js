// Paste this into the devtools console and all videos currently visible will be downloaded.

Array.from($('.recording-action-icons')).map((el, i) => setTimeout(
    () => el.children[1]
        .children[0]
        .children[1]
        .children[0]
        .children[0]
        .click(),
    i * 1500
))
