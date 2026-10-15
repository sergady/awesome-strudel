### J

- `jux`
- `juxBy`
- `juxby`
- `juxFlip`
- `juxflip`
- `juxFlipBy`
- `juxflipby`

## Entries

### jux

**Call:** `.jux()`.

The jux function creates strange stereo effects, by applying a function to a pattern, but only in the right-hand channel.


s("bd lt [~ ht] mt cp ~ bd hh").jux(rev)

s("bd lt [~ ht] mt cp ~ bd hh").jux(press)

s("bd lt [~ ht] mt cp ~ bd hh").jux(iter(4))

Source: `packages/core/pattern.mjs`.

### juxBy

**Call:** `.juxBy(…)`. Alias: `juxby`.

Jux with adjustable stereo width. 0 = mono, 1 = full stereo.

```js
s("bd lt [~ ht] mt cp ~ bd hh").juxBy("<0 .5 1>/2", rev)
```

Source: `packages/core/pattern.mjs`.

### juxby

**Call:** `.juxby()`. Same as `juxBy`.

Jux with adjustable stereo width. 0 = mono, 1 = full stereo.

```js
s("bd lt [~ ht] mt cp ~ bd hh").juxBy("<0 .5 1>/2", rev)
```

Source: `packages/core/pattern.mjs`.

### juxFlip

**Call:** `.juxFlip(…)`. Aliases: `juxflip`, `flux`.

Like jux, but flips the ears each cycle.

```js
s("bd lt [~ ht] mt cp ~ bd hh").juxFlip(rev)
```

```js
s("bd lt [~ ht] mt cp ~ bd hh").juxFlip(press)
```

```js
s("bd lt [~ ht] mt cp ~ bd hh").juxFlip(iter(4))
```

Source: `packages/core/pattern.mjs`.

### juxflip

**Call:** `.juxflip()`. Same as `juxFlip`.

Like jux, but flips the ears each cycle.

```js
s("bd lt [~ ht] mt cp ~ bd hh").juxFlip(rev)
```

```js
s("bd lt [~ ht] mt cp ~ bd hh").juxFlip(press)
```

```js
s("bd lt [~ ht] mt cp ~ bd hh").juxFlip(iter(4))
```

Source: `packages/core/pattern.mjs`.

### juxFlipBy

**Call:** `.juxFlipBy(…)`. Aliases: `juxflipby`, `fluxBy`, `fluxby`.

Like juxBy, except it flips the ears each cycle.

```js
s("bd lt [~ ht] mt cp ~ bd hh").juxFlipBy(".8", rev)
```

Source: `packages/core/pattern.mjs`.

### juxflipby

**Call:** `.juxflipby()`. Same as `juxFlipBy`.

Like juxBy, except it flips the ears each cycle.

```js
s("bd lt [~ ht] mt cp ~ bd hh").juxFlipBy(".8", rev)
```

Source: `packages/core/pattern.mjs`.
