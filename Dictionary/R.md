### R

- `rand`
- `randL`
- `range`
- `range2`
- `rangex`
- `rarely`
- `ratio`
- `rdim` — alias of `roomdim`
- `real`
- `rel` — alias of `release`
- `release`
- `repeatCycles`
- `rescale`
- `resonance`
- `rev`
- `revv`
- `rfade` — alias of `roomfade`
- `rib`
- `ribbon`
- `ring`
- `ringdf`
- `ringf`
- `rlp` — alias of `roomlp`
- `room`
- `roomdim`
- `roomfade`
- `roomlp`
- `roomsize`
- `rootNotes`
- `rotA` — alias of `rotationAlpha`
- `rotationAlpha`
- `rotationBeta`
- `rotationGamma`
- `rotationX` — alias of `rotationBeta`
- `rotationY` — alias of `rotationGamma`
- `rotationZ` — alias of `rotationAlpha`
- `rotB` — alias of `rotationBeta`
- `rotG` — alias of `rotationGamma`
- `rotX` — alias of `rotationBeta`
- `rotY` — alias of `rotationGamma`
- `rotZ` — alias of `rotationAlpha`
- `round`
- `rsize` — alias of `roomsize`

## Entries

### rand

**Call:** `rand`.

A continuous pattern of random numbers, between 0 and 1.

```js
// randomly change the cutoff
s("bd*4,hh*8").cutoff(rand.range(500,8000))
```

Source: `packages/core/signal.mjs`.

### randL

**Call:** `randL(n)`.

Creates a list of random numbers of the given length

```js
s("saw").seg(16).n(irand(12)).scale("F1:minor")
  .partials(randL(8))
```

Source: `packages/core/signal.mjs`.

### range

**Call:** `.range(…)`.

Assumes a numerical pattern, containing unipolar values in the range 0 .. 1.
Returns a new pattern with values scaled to the given min/max range.
Most useful in combination with continuous patterns.

```js
s("[bd sd]*2,hh*8")
.cutoff(sine.range(500,4000))
```

Source: `packages/core/pattern.mjs`.

### range2

**Call:** `.range2(…)`.

Assumes a numerical pattern, containing bipolar values in the range -1 .. 1
Returns a new pattern with values scaled to the given min/max range.

```js
s("[bd sd]*2,hh*8")
.cutoff(sine2.range2(500,4000))
```

Source: `packages/core/pattern.mjs`.

### rangex

**Call:** `.rangex(…)`.

Assumes a numerical pattern, containing unipolar values in the range 0 .. 1
Returns a new pattern with values scaled to the given min/max range,
following an exponential curve.

```js
s("[bd sd]*2,hh*8")
.cutoff(sine.rangex(500,4000))
```

Source: `packages/core/pattern.mjs`.

### rarely

**Call:** `.rarely(…)`.

Shorthand for `.sometimesBy(0.25, fn)`

```js
s("hh*8").rarely(x=>x.speed("0.5"))
```

Source: `packages/core/signal.mjs`.

### ratio

**Call:** `.ratio(…)`.

Allows dividing numbers via list notation using ":".
Returns a new pattern with just numbers.

```js
ratio("1, 5:4, 3:2").mul(110)
.freq().s("piano")
```

Source: `packages/core/pattern.mjs`.

### real

**Call:** `.real(amount)`.

Real part of a spectrum, registered as a pair with `imag`. The browser synth does not read this control. It is registered with the other SuperDirt effects, next to `waveloss`.

```js
note("c3").s("sawtooth").real("<0 .5 1>").osc().gain(0.15)
```

Source: `packages/core/controls.mjs`.

### release

**Call:** `.release(time)`. Alias: `rel`.

Amplitude envelope release time: The time it takes after the offset to go from sustain level to zero.

```js
note("c3 e3 g3 c4").release("<0 .1 .4 .6 1>/2")
```

Source: `packages/core/controls.mjs`.

### repeatCycles

**Call:** `.repeatCycles(…)`.

Repeats each cycle the given number of times.

```js
note(irand(12).add(34)).segment(4).repeatCycles(2).s("gm_acoustic_guitar_nylon")
```

Source: `packages/core/pattern.mjs`.

### rescale

**Call:** `.rescale(factor)`.

Multiplies the drawing controls `x`, `y`, `w`, and `h` by the same factor.

```js
s("rect").x(0.25).y(0.25).w(0.5).h(0.5).rescale("<1 .5 .25>")
```

Source: `packages/draw/animate.mjs`.

### resonance

**Call:** `.resonance(q)`. Same as `lpq`.

Controls the **l**ow-**p**ass **q**-value.

```js
s("bd sd [~ bd] sd,hh*8").lpf(2000).lpq("<0 10 20 30>")
```

Source: `packages/core/controls.mjs`.

### rev

**Call:** `.rev()`.

Reverse all cycles in a pattern. See also `revv` for reversing a whole pattern.

```js
note("c d e g").rev()
```

Source: `packages/core/pattern.mjs`.

### revv

**Call:** `.revv()`.

Reverse a whole pattern. See also `rev` for reversing each cycle.

```js
// This is the same as `<[g e] [d c]>`. If `rev()` is used, you get
// the same as `<[d c] [g e]>`, where each cycle reverses, but the order of
// cycles stays the same.
note("<[c d] [e g]>").revv()
```

Source: `packages/core/pattern.mjs`.

### rib

**Call:** `.rib(offset, cycles)`. Same as `ribbon`.

Loops the pattern inside an `offset` for `cycles`.
If you think of the entire span of time in cycles as a ribbon, you can cut a single piece and loop it.

```js
note("<c d e f>").ribbon(1, 2)
```

```js
// Looping a portion of randomness
n(irand(8).segment(4)).scale("c:pentatonic").ribbon(1337, 2)
```

```js
// rhythm generator
s("bd!16?").ribbon(29,.5)
```

Source: `packages/core/pattern.mjs`.

### ribbon

**Call:** `.ribbon(offset, cycles)`. Alias: `rib`.

Loops the pattern inside an `offset` for `cycles`.
If you think of the entire span of time in cycles as a ribbon, you can cut a single piece and loop it.

```js
note("<c d e f>").ribbon(1, 2)
```

```js
// Looping a portion of randomness
n(irand(8).segment(4)).scale("c:pentatonic").ribbon(1337, 2)
```

```js
// rhythm generator
s("bd!16?").ribbon(29,.5)
```

Source: `packages/core/pattern.mjs`.

### ring

**Call:** `.ring(mix)`.

Ring-modulation mix. The browser synth does not read this control. It is registered with the other SuperDirt effects, next to `waveloss`.

```js
note("c3").s("sawtooth").ring("<0 .4 .8>").osc().gain(0.15)
```

Source: `packages/core/controls.mjs`.

### ringdf

**Call:** `.ringdf(amount)`.

A ring-modulation control registered with `ring` and `ringf`. The browser synth does not read this control. It is registered with the other SuperDirt effects, next to `waveloss`.

```js
note("c3").s("sawtooth").ring(0.6).ringf(200).ringdf("<0 20 80>").osc().gain(0.15)
```

Source: `packages/core/controls.mjs`.

### ringf

**Call:** `.ringf(frequency)`.

Ring-modulation frequency. The browser synth does not read this control. It is registered with the other SuperDirt effects, next to `waveloss`.

```js
note("c3").s("sawtooth").ring(0.7).ringf("<50 200 700>").osc().gain(0.15)
```

Source: `packages/core/controls.mjs`.

### room

**Call:** `.room(level)`.

Sets the level of reverb.

When using mininotation, you can also optionally add the 'size' parameter, separated by ':'.

```js
s("bd sd [~ bd] sd").room("<0 .2 .4 .6 .8 1>")
```

```js
s("bd sd [~ bd] sd").room("<0.9:1 0.9:4>")
```

Source: `packages/core/controls.mjs`.

### roomdim

**Call:** `.roomdim(frequency)`. Alias: `rdim`.

Reverb lowpass frequency at -60dB (in hertz).
When this property is changed, the reverb will be recaculated, so only change this sparsely..

```js
s("bd sd [~ bd] sd").room(0.5).rlp(10000).rdim(8000)
```

```js
s("bd sd [~ bd] sd").room(0.5).rlp(5000).rdim(400)
```

Source: `packages/core/controls.mjs`.

### roomfade

**Call:** `.roomfade(seconds)`. Alias: `rfade`.

Reverb fade time (in seconds).
When this property is changed, the reverb will be recaculated, so only change this sparsely..

```js
s("bd sd [~ bd] sd").room(0.5).rlp(10000).rfade(0.5)
```

```js
s("bd sd [~ bd] sd").room(0.5).rlp(5000).rfade(4)
```

Source: `packages/core/controls.mjs`.

### roomlp

**Call:** `.roomlp(frequency)`. Alias: `rlp`.

Reverb lowpass starting frequency (in hertz).
When this property is changed, the reverb will be recaculated, so only change this sparsely..

```js
s("bd sd [~ bd] sd").room(0.5).rlp(10000)
```

```js
s("bd sd [~ bd] sd").room(0.5).rlp(5000)
```

Source: `packages/core/controls.mjs`.

### roomsize

**Call:** `.roomsize(size)`. Aliases: `rsize`, `sz`, `size`.

Sets the room size of the reverb, see `room`.
When this property is changed, the reverb will be recaculated, so only change this sparsely..

```js
s("bd sd [~ bd] sd").room(.8).rsize(1)
```

```js
s("bd sd [~ bd] sd").room(.8).rsize(4)
```

Source: `packages/core/controls.mjs`.

### rootNotes

**Call:** `.rootNotes(octave)`.

Maps the chords of the incoming pattern to root notes in the given octave.

```js
"<C^7 A7 Dm7 G7>".rootNotes(2).note()
```

Source: `packages/tonal/voicings.mjs`.

### rotationAlpha

**Call:** `rotationAlpha`. Aliases: `rotA`, `rotZ`, `rotationZ`.

The device's rotation around the alpha-axis value ranges from 0 to 1.

```js
n(rotationAlpha.segment(4).range(0,7)).scale("C:minor")
```

Source: `packages/motion/motion.mjs`.

### rotationBeta

**Call:** `rotationBeta`. Aliases: `rotB`, `rotX`, `rotationX`.

The device's rotation around the beta-axis value ranges from 0 to 1.

```js
n(rotationBeta.segment(4).range(0,7)).scale("C:minor")
```

Source: `packages/motion/motion.mjs`.

### rotationGamma

**Call:** `rotationGamma`. Aliases: `rotG`, `rotY`, `rotationY`.

The device's rotation around the gamma-axis value ranges from 0 to 1.

```js
n(rotationGamma.segment(4).range(0,7)).scale("C:minor")
```

Source: `packages/motion/motion.mjs`.

### round

**Call:** `.round()`.

Assumes a numerical pattern. Returns a new pattern with all values rounded
to the nearest integer.

```js
n("0.5 1.5 2.5".round()).scale("C:major")
```

Source: `packages/core/pattern.mjs`.
