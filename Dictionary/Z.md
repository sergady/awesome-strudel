### Z

- `zcrush`
- `zdelay`
- `zmod`
- `znoise`
- `zoom`
- `zoomArc`
- `zoomarc`
- `zoomIn`
- `zrand`
- `zzfx`

## Entries

### zcrush

**Call:** `.zcrush(amount)`.

Bit crush of a ZZFX sound. The source says it is like `crush`, scaled differently. It is one of the ZZFX parameters, not the general `crush` control.

```js
s("z_sawtooth").note("c3").zcrush("<0 4 10>").gain(0.2)
```

Source: `packages/core/controls.mjs`.

### zdelay

**Call:** `.zdelay(time)`.

Delay inside a ZZFX sound, in the synth's own time unit. It is not the pattern `delay` send.

```js
s("z_sine").note("c3").zdelay("<0 .05 .15>").gain(0.2)
```

Source: `packages/core/controls.mjs`.

### zmod

**Call:** `.zmod(amount)`.

Modulation amount of a ZZFX sound.

```js
s("z_sawtooth").note("c3").zmod("<0 .2 .6>").gain(0.2)
```

Source: `packages/core/controls.mjs`.

### znoise

**Call:** `.znoise(amount)`.

Noise mixed into a ZZFX sound. The source comment calls it frequency fog.

```js
s("z_sine").note("c3").znoise("<0 .2 .6>").gain(0.2)
```

Source: `packages/core/controls.mjs`.

### zoom

**Call:** `.zoom()`.

Plays a portion of a pattern, specified by the beginning and end of a time span. The new resulting pattern is played over the time period of the original pattern:



s("bd*2 hh*3 [sd bd]*2 perc").zoom(0.25, 0.75)
// s("hh*3 [sd bd]*2") // equivalent

Source: `packages/core/pattern.mjs`.

### zoomArc

**Call:** `.zoomArc(span)`.

Same function as `zoom`, reading `begin` and `end` from one value. `zoomarc` is the same function. The slice is stretched to fill the cycle.

```js
note("c4 d4 e4 f4 g4 a4").s("triangle").zoom(0, 0.5).gain(0.2)
```

Source: `packages/core/pattern.mjs`.

### zoomarc

**Call:** `.zoomarc(span)`.

Same function as `zoomArc`.

```js
note("c4 d4 e4 f4 g4 a4").s("triangle").zoomarc({begin: 0, end: 0.5}).gain(0.2)
```

Source: `packages/core/pattern.mjs`.

### zoomIn

**Call:** `.zoomIn(factor)`.

Drawing zoom toward the center. It multiplies `x`, `y`, `w`, and `h` by `factor`, then shifts `x` and `y` by `(1 - factor) / 2`.

```js
s("rect").x(0.1).y(0.1).w(0.8).h(0.8).zoomIn("<1 .6 .3>")
```

Source: `packages/draw/animate.mjs`.

### zrand

**Call:** `.zrand(amount)`.

Random detune of a ZZFX sound. The synth picks a frequency inside a range set by this amount.

```js
s("z_sine").note("c3*8").zrand("<0 .05 .3>").gain(0.2)
```

Source: `packages/core/controls.mjs`.

### zzfx

**Call:** `.zzfx(params)`.

Raw ZZFX parameter list. When it is set, it replaces the parameters built from `zrand`, `curve`, `slide`, `pitchJump`, `znoise`, `zmod`, `zcrush`, `zdelay`, and the envelope. Use it with `s("zzfx")` or a `z_` waveform.

```js
s("zzfx").zzfx([0.2, 0, 220, 0, 0.1, 0.1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0.4, 0, 0]).gain(0.3)
```

Source: `packages/core/controls.mjs`.
