### W

- `warp`
- `warpatt` — alias of `warpattack`
- `warpattack`
- `warpdc`
- `warpdec` — alias of `warpdecay`
- `warpdecay`
- `warpdepth`
- `warpenv`
- `warpmode`
- `warprate`
- `warprel` — alias of `warprelease`
- `warprelease`
- `warpshape`
- `warpskew`
- `warpsus` — alias of `warpsustain`
- `warpsustain`
- `warpsync`
- `waveloss`
- `wavetablePhaseRand` — alias of `wtphaserand`
- `wavetablePosition` — alias of `wt`
- `wavetableWarp` — alias of `warp`
- `wavetableWarpMode` — alias of `warpmode`
- `weave`
- `weaveWith`
- `when`
- `whenKey`
- `withBase`
- `within`
- `wordfall`
- `worklet`
- `wt`
- `wtatt` — alias of `wtattack`
- `wtattack`
- `wtdc`
- `wtdec` — alias of `wtdecay`
- `wtdecay`
- `wtdepth`
- `wtenv`
- `wtphaserand`
- `wtrate`
- `wtrel` — alias of `wtrelease`
- `wtrelease`
- `wtshape`
- `wtskew`
- `wtsus` — alias of `wtsustain`
- `wtsustain`
- `wtsync`

## Entries

### warp

**Call:** `.warp(amount)`. Alias: `wavetableWarp`.

Amount of warp (alteration of the waveform) to apply to the wavetable oscillator

```js
s("basique").bank("wt_digital").seg(8).note("F1").warp("0 0.25 0.5 0.75 1")
  .warpmode("spin")
```

Source: `packages/core/controls.mjs`.

### warpattack

**Call:** `.warpattack(time)`. Alias: `warpatt`.

Attack time of the wavetable oscillator's warp envelope

Source: `packages/core/controls.mjs`.

### warpdc

**Call:** `.warpdc(dcoffset)`.

DC offset of the LFO for the wavetable oscillator's warp

Source: `packages/core/controls.mjs`.

### warpdecay

**Call:** `.warpdecay(time)`. Alias: `warpdec`.

Decay time of the wavetable oscillator's warp envelope

Source: `packages/core/controls.mjs`.

### warpdepth

**Call:** `.warpdepth(depth)`.

Depth of the LFO for the wavetable oscillator's warp

Source: `packages/core/controls.mjs`.

### warpenv

**Call:** `.warpenv(amount)`.

Amount of envelope applied wavetable oscillator's position envelope

Source: `packages/core/controls.mjs`.

### warpmode

**Call:** `.warpmode(mode)`. Alias: `wavetableWarpMode`.

Type of warp (alteration of the waveform) to apply to the wavetable oscillator.

The current options are: none, asym, bendp, bendm, bendmp, sync, quant, fold, pwm, orbit,
spin, chaos, primes, binary, brownian, reciprocal, wormhole, logistic, sigmoid, fractal, flip

```js
s("morgana").bank("wt_digital").seg(8).note("F1").warp("0 0.25 0.5 0.75 1")
  .warpmode("<asym bendp spin logistic sync wormhole brownian>*2")
```

Source: `packages/core/controls.mjs`.

### warprate

**Call:** `.warprate(rate)`.

Rate of the LFO for the wavetable oscillator's warp

Source: `packages/core/controls.mjs`.

### warprelease

**Call:** `.warprelease(time)`. Alias: `warprel`.

Release time of the wavetable oscillator's warp envelope

Source: `packages/core/controls.mjs`.

### warpshape

**Call:** `.warpshape(shape)`.

Shape of the LFO for the wavetable oscillator's warp

Source: `packages/core/controls.mjs`.

### warpskew

**Call:** `.warpskew(skew)`.

Skew of the LFO for the wavetable oscillator's warp

Source: `packages/core/controls.mjs`.

### warpsustain

**Call:** `.warpsustain(gain)`. Alias: `warpsus`.

Sustain time of the wavetable oscillator's warp envelope

Source: `packages/core/controls.mjs`.

### warpsync

**Call:** `.warpsync(rate)`.

cycle synced rate of the LFO for the wavetable warp position

Source: `packages/core/controls.mjs`.

### waveloss

**Call:** `.waveloss()`.

// TODO: find out how it works
Made by Calum Gunn. Divides an audio stream into tiny segments, using the signal's zero-crossings as segment boundaries, and discards a fraction of them. Takes a number between 1 and 100, denoted the percentage of segments to drop. The SuperCollider manual describes the Waveloss effect this way:

Divide an audio stream into tiny segments, using the signal's zero-crossings as segment boundaries, and discard a fraction of them (i.e. replace them with silence of the same length). The technique was described by Trevor Wishart in a lecture. Parameters: the filter drops drop out of out of chunks. mode can be 1 to drop chunks in a simple deterministic fashion (e.g. always dropping the first 30 out of a set of 40 segments), or 2 to drop chunks randomly but in an appropriate proportion.)

mode: ?
waveloss: ?

Source: `packages/core/controls.mjs`.

### weave

**Call:** `.weave(…)`.

Takes a time duration followed by one or more patterns, and shifts the given patterns in time, so they are
distributed equally over the given time duration. They are then combined with the pattern 'weave' is called on, after it has been stretched out (i.e. slowed down by) the time duration.

```js
pan(saw).weave(4, s("bd(3,8)"), s("~ sd"))
```

```js
n("0 1 2 3 4 5 6 7").weave(8, s("bd(3,8)"), s("~ sd"))

addToPrototype('weave', function (t, ...pats) {
  return this.weaveWith(t, ...pats.map((x) => set.out(x)));
});
```

Source: `packages/core/pattern.mjs`.

### weaveWith

**Call:** `weaveWith`.

Like 'weave', but accepts functions rather than patterns, which are applied to the pattern.

Source: `packages/core/pattern.mjs`.

### when

**Call:** `.when(binary_pat, func)`.

Applies the given function whenever the given pattern is in a true state.

```js
"c3 eb3 g3".when("<0 1>/2", x=>x.sub("5")).note()
```

Source: `packages/core/pattern.mjs`.

### whenKey

**Call:** `.whenKey(…)`.

Do something on a keypress, or array of keypresses
[Key name reference](https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values)

```js
s("bd(5,8)").whenKey("Control:j", x => x.segment(16).color("red")).whenKey("Control:i", x => x.fast(2).color("blue"))
```

Source: `packages/core/signal.mjs`.

### withBase

**Call:** `.withBase(base)`.

Assumes pattern of frequencies tuned to some `base` frequency, such as the output of `xen`
Because `xen` defaults to `220Hz`, so will `withBase`.
but you can specify a different original base with the standard optional array syntax '`:`'

```js
i("[0 1 2 3] [3 4] [4 3 2 1]").xen("hexany23").withBase("<220 [300 200]>")
```

```js
mini([1 / 1, 16 / 15, 9 / 8, 6 / 5, 5 / 4].join(' ')).withBase("220:1")
// mini([1 / 1, 16 / 15, 9 / 8, 6 / 5, 5 / 4].join(' ')).mul(220).freq()
```

Source: `packages/xen/xen.mjs`.

### within

**Call:** `.within(start, end, func)`.

Use within to apply a function to only a part of a pattern.

Source: `packages/core/pattern.mjs`.

### wordfall

**Call:** `.wordfall()`.

Displays a vertical pianoroll with event labels.
Supports all the same options as pianoroll.

Source: `packages/draw/pianoroll.mjs`.

### worklet

**Call:** `.worklet(src, inputs)`.

Creates a worklet effect. Typically derived by writing K(...) in the REPL which will parse
Kabelsalat code.

Source: `packages/core/pattern.mjs`.

### wt

**Call:** `.wt(position)`. Alias: `wavetablePosition`.

Position in the wavetable of the wavetable oscillator

```js
s("wt_digital").seg(8).note("F1").wt("0 0.25 0.5 0.75 1")
```

Source: `packages/core/controls.mjs`.

### wtattack

**Call:** `.wtattack(time)`. Alias: `wtatt`.

Attack time of the wavetable oscillator's position envelope

Source: `packages/core/controls.mjs`.

### wtdc

**Call:** `.wtdc(dcoffset)`.

DC offset of the LFO for the wavetable oscillator's position

Source: `packages/core/controls.mjs`.

### wtdecay

**Call:** `.wtdecay(time)`. Alias: `wtdec`.

Decay time of the wavetable oscillator's position envelope

Source: `packages/core/controls.mjs`.

### wtdepth

**Call:** `.wtdepth(depth)`.

Depth of the LFO for the wavetable oscillator's position

Source: `packages/core/controls.mjs`.

### wtenv

**Call:** `.wtenv(amount)`.

Amount of envelope applied wavetable oscillator's position envelope

Source: `packages/core/controls.mjs`.

### wtphaserand

**Call:** `.wtphaserand(amount)`. Alias: `wavetablePhaseRand`.

Amount of randomness of the initial phase of the wavetable oscillator.

```js
s("basique").bank("wt_digital").seg(16).wtphaserand("<0 1>")
```

Source: `packages/core/controls.mjs`.

### wtrate

**Call:** `.wtrate(rate)`.

Rate of the LFO for the wavetable oscillator's position

Source: `packages/core/controls.mjs`.

### wtrelease

**Call:** `.wtrelease(time)`. Alias: `wtrel`.

Release time of the wavetable oscillator's position envelope

Source: `packages/core/controls.mjs`.

### wtshape

**Call:** `.wtshape(shape)`.

Shape of the LFO for the wavetable oscillator's position

Source: `packages/core/controls.mjs`.

### wtskew

**Call:** `.wtskew(skew)`.

Skew of the LFO for the wavetable oscillator's position

Source: `packages/core/controls.mjs`.

### wtsustain

**Call:** `.wtsustain(gain)`. Alias: `wtsus`.

Sustain time of the wavetable oscillator's position envelope

Source: `packages/core/controls.mjs`.

### wtsync

**Call:** `.wtsync(rate)`.

cycle synced rate of the LFO for the wavetable oscillator's position

Source: `packages/core/controls.mjs`.
