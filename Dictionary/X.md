### X

- `xen`
- `xfade`
- `xsdelay`

## Entries

### xen

**Call:** `.xen(scaleNameOrRatios)`.

Assumes a numerical pattern of scale steps, and a scale. Scales accepted are all preset scale names of `tune`, arbitrary edos such as 31edo, or an array of frequency ratios. Assumes scales repeat at octave (2/1). Returns a new pattern with all values mapped to their associated frequency, assuming a base frequency of 220hz. See first 4 examples for the different ways you can input a scale into `xen`

```js
// A minor triad in 31edo:
i("0 8 18").xen("31edo").piano()
```

```js
// You can also use xen with frequency ratios.
// This is equivalent to the above:
i("0 1 2").xen([
  Math.pow(2, 0/31),
  Math.pow(2, 8/31),
  Math.pow(2, 18/31),
]).piano()
```

```js
// However, with the above you won't get highlighting of the scale indices,
// instead you could do something like:
i("[<2 ->, 0 1 <- 2> 3]*2").xen([
  "1:1", // tonic
  "5:4", // Major 3rd
  "[3:2 4:3]", // Perfect 5th, 4th
  "5:3" // Major 6th
]).s("tri")
```

```js
// xen also supports all scale names that
// tune does:
i("0 1 2 3 4 5").xen("hexany15")
// equiv to:
// "0 1 2 3 4 5".tune("hexany15").mul("220").freq()
```

```js
i("0 1 2 3 4 5 6 7").xen("<5edo 10edo 15edo hexany15>")
```

Source: `packages/xen/xen.mjs`.

### xfade

**Call:** `.xfade(…)`.

Cross-fades between left and right from 0 to 1:
- 0 = (full left, no right)
- .5 = (both equal)
- 1 = (no left, full right)

```js
xfade(s("bd*2"), "<0 .25 .5 .75 1>", s("hh*8"))
```

Source: `packages/core/pattern.mjs`.

### xsdelay

**Call:** `.xsdelay(time)`.

A delay registered with `tsdelay`. The browser synth does not read this control. It is registered with the other SuperDirt effects, next to `waveloss`.

```js
note("c3 ~").s("sawtooth").xsdelay("<0 .25 .5>").osc().gain(0.15)
```

Source: `packages/core/controls.mjs`.
