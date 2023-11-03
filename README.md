# Other style for Grappelli

Black / White with CSS variables

Only for: django-grappelli==3.0.8

Base style:

```
:root {
    --font-main: BlinkMacSystemFont, -apple-system, "Segoe UI", Roboto, Oxygen, Ubuntu,Cantarell, "Fira Sans", "Droid Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
    --c-bgr: #222;
    --c-btn: white;
    --c-bgr-btn: #222;
    --c-bgr-btn-border: #777;
    --c-bgr-btn-hover: #333;
    --f-color: #444;
    --f-color-dark: #222;
    --link-color-hover: #666;
    --link-color: #212121;
    --header-color: white;
    --header-bgr: #222;

    --c-bar: #222;
    --c-bar-bgr: #ccc;
    --c-bar-bgr-closed: #ccc;
    --c-bar-bgr-hover: #c3c3c3;
}
```

Add another font:

Monospace:
```
--font-main: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace
```

Load fonts:

@font-face {
  font-family: "FontName";
  src: url("fontname-bold.woff2") format("woff2");
  font-weight: bold;
}
@font-face {
  font-family: "FontName";
  src: url("fontname-regular.woff2") format("woff2");
  font-weight: normal;
}
