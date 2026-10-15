### E

- `early`
- `echo`
- `echoWith`
- `echowith`
- `edoScale`
- `eish`
- `end`
- `enhance`
- `env`
- `eq`
- `eqt`
- `euclid`
- `euclidish`
- `euclidLegato`
- `euclidLegatoRot`
- `euclidRot`
- `euclidrot`
- `every`
- `expression`

## Entries

### early

**Call:** `.early(cycles)`.

Nudge a pattern to start earlier in time. Equivalent of Tidal's <~ operator

```js
"bd ~".stack("hh ~".early(.1)).s()
```

Source: `packages/core/pattern.mjs`.

### echo

**Call:** `.echo(times, time, feedback)`.

Superimpose and offset multiple times, gradually decreasing the velocity

```js
s("bd sd").echo(3, 1/6, .8)
```

Source: `packages/core/pattern.mjs`.

### echoWith

**Call:** `.echoWith(times, time, func)`. Aliases: `echowith`, `stutWith`, `stutwith`.

Superimpose and offset multiple times, applying the given function each time.

```js
"<0 [2 4]>"
.echoWith(4, 1/8, (p,n) => p.add(n*2))
.scale("C:minor").note()
```

Source: `packages/core/pattern.mjs`.

### echowith

**Call:** `.echowith(times, time, func)`. Same as `echoWith`.

Superimpose and offset multiple times, applying the given function each time.

```js
"<0 [2 4]>"
.echoWith(4, 1/8, (p,n) => p.add(n*2))
.scale("C:minor").note()
```

Source: `packages/core/pattern.mjs`.

### edoScale

**Call:** `.edoScale(scale)`.

Turns numbers into notes in the given EDO scale (zero indexed).

An EDO scale definition looks like this:

e.g. C:LLsLLLs:2:1 <- this is the C major scale, 12 EDO

e.g. C:LLsLLL:3:1 <- this is the Gorgo 6 note scale, 16 EDO

An EDO scale, e.g. C:LLsLLLs:2:1, consists of a root note (e.g. C)
followed by semicolon (':')
and then a [Large/small step notation sequence](https://en.xen.wiki/w/MOS_scale)
(e.g. LLsLLLs)
followed by semicolon, then the large step size (e.g. 2)
followed by semicolon, then the small step size (e.g. 1).

The number of divisions of the octave is calculated as the sum
of the steps in the EDO scale definition.

e.g. C:LLsLLLs:2:1 is 2+2+1+2+2+2+1 = 12 EDO, 7 note scale

e.g. C:LLsLLL:3:1 is 3+3+1+3+3+3 = 16 EDO, 6 note scale

The root note defaults to octave 3, if no octave number is given.

```js
n("0 2 4 6 4 2").edoScale("C:LLsLLLs:2:1")
```

```js
n("[0,7] 4 [2,7] 4")
.edoScale("G2:<LLsLLL LLLLsL>:3:1")
.s("piano")._pitchwheel()
```

```js
n(rand.range(0,5).segment(6))
.edoScale("<G2 C3>:LLsLL:3:1")
.s("piano")._pitchwheel()
```

Source: `packages/edo/edo.mjs`.

### eish

**Call:** `.eish(pulses, steps, groove)`. Same as `euclidish`.

A 'euclid' variant with an additional parameter that morphs the resulting
rhythm from 0 (no morphing) to 1 (completely 'even'). For example
`sound("bd").euclidish(3,8,0)` would be the same as
`sound("bd").euclid(3,8)`, and `sound("bd").euclidish(3,8,1)` would be the
same as `sound("bd bd bd")`. `sound("bd").euclidish(3,8,0.5)` would have a
groove somewhere between.
Inspired by the work of Malcom Braff.

```js
sound("hh").euclidish(7,12,sine.slow(8))
.pan(sine.slow(8))
```

Source: `packages/core/euclid.mjs`.

### end

**Call:** `.end(length)`.

The same as .begin, but cuts off the end off each sample.

```js
s("bd*2,oh*4").end("<.1 .2 .5 1>").fast(2)
```

Source: `packages/core/controls.mjs`.

### enhance

**Call:** `.enhance(amount)`.

Spectral enhance. The browser synth does not read this control. It is registered with the other SuperDirt effects, next to `waveloss`.

```js
note("c3").s("sawtooth").enhance("<0 .5 1>").osc().gain(0.15)
```

Source: `packages/core/controls.mjs`.

### env

**Call:** `.env(config, id)`.

Configures an envelope. Can be called in sequence like pat.env(...).env(...) to set up multiple envelopes
There are two ways to declare which control will be modulated:
1. Explicitly put `control` in the config (e.g. `env({ c: "lpf" })`)
2. If the control parameter is absent, the control _immediately before_ the `env` call will be used
  (e.g. `s("saw").lpf(500).env({ a: 1 })` to modulate `lpf`)

Modulators can be referred to by `id` so that they can be updated later e.g. inside
a `sometimes`. See example below.

```js
s("saw").note("F1").lpf(500).env({ a: 1 })
```

```js
s("saw").env({ d: 1 }).note("F1")
  .lpq(4).lpf(50)
  .env({ a: 0.1, d: 1, ac: 0.8, dc: 0.3, depth: 50 })
```

```js
s("saw").lpf(500).diode(0.3)
  .env({ c: "lpf", a: 0.5, d: 0.5 })
```

```js
s("pulse").lpf(500).env({ a: 1 })
  .env({ c: "s", a: 1 })
  .diode(0.3)
  .sometimes(x => x.env({ a: "0.5" }, 1)) // envelope #1 (0-indexed)
```

```js
s("pulse").lpf(500).env({ a: 1 }, 'lpf_mod')
  .env({ c: "s", a: 1 })
  .diode(0.3)
  .sometimes(x => x.env({ a: "0.5" }, 'lpf_mod'))
```

Source: `packages/core/controls.mjs`.

### eq

**Call:** `eq(a, b)`.

performs a == b

Source: `packages/core/pattern.mjs`.

### eqt

**Call:** `eqt(a, b)`.

performs a === b (strictly equal)

Source: `packages/core/pattern.mjs`.

### euclid

**Call:** `.euclid(pulses, steps)`.

Changes the structure of the pattern to form an Euclidean rhythm.
Euclidean rhythms are rhythms obtained using the greatest common
divisor of two numbers.  They were described in 2004 by Godfried
Toussaint, a Canadian computer scientist.  Euclidean rhythms are
really useful for computer/algorithmic music because they can
describe a large number of rhythms with a couple of numbers.

A negative number of pulses inverts the pattern
so pulses happen in the gaps of the normal euclidean rhythm.

A negative number of steps changes it into `euclidLegato`.

```js
// The Cuban tresillo pattern.
note("c3").euclid(3,8)
```

Source: `packages/core/euclid.mjs`.

### euclidish

**Call:** `.euclidish(pulses, steps, groove)`. Alias: `eish`.

A 'euclid' variant with an additional parameter that morphs the resulting
rhythm from 0 (no morphing) to 1 (completely 'even'). For example
`sound("bd").euclidish(3,8,0)` would be the same as
`sound("bd").euclid(3,8)`, and `sound("bd").euclidish(3,8,1)` would be the
same as `sound("bd bd bd")`. `sound("bd").euclidish(3,8,0.5)` would have a
groove somewhere between.
Inspired by the work of Malcom Braff.

```js
sound("hh").euclidish(7,12,sine.slow(8))
.pan(sine.slow(8))
```

Source: `packages/core/euclid.mjs`.

### euclidLegato

**Call:** `.euclidLegato(pulses, steps)`.

Similar to `euclid`, but each pulse is held until the next pulse,
so there will be no gaps.

A negative number of steps changes it into `euclid`.

```js
note("c3").euclidLegato(3,8)
```

Source: `packages/core/euclid.mjs`.

### euclidLegatoRot

**Call:** `.euclidLegatoRot(pulses, steps, rotation)`.

Similar to `euclid`, but each pulse is held until the next pulse,
so there will be no gaps, and has an additional parameter for 'rotating'
the resulting sequence.

A negative number of steps changes it into `euclidRot`.

```js
note("c3").euclidLegatoRot(3,5,2)
```

Source: `packages/core/euclid.mjs`.

### euclidRot

**Call:** `.euclidRot(pulses, steps, rotation)`.

Like `euclid`, but has an additional parameter for 'rotating' the resulting sequence.

```js
// A Samba rhythm necklace from Brazil
note("c3").euclidRot(3,16,14)
```

Source: `packages/core/euclid.mjs`.

### euclidrot

**Call:** `.euclidrot(pulses, steps, rotation)`.

Same function as `euclidRot`. Distributes `pulses` across `steps` as evenly as possible, then rotates the pattern by `rotation` steps.

```js
note("c3").s("triangle").euclidrot(3, 8, 1).decay(0.08).sustain(0).gain(0.2)
```

Source: `packages/core/euclid.mjs`.

### every

**Call:** `.every(n, func)`.

An alias for `firstOf`

```js
note("c3 d3 e3 g3").every(4, x=>x.rev())
```

Source: `packages/core/pattern.mjs`.

### expression

**Call:** `.expression(amount)`.

MIDI expression control. It is registered next to `sustainpedal`. The MIDI output in this checkout does not send it.

```js
note("c4 e4 g4").expression(0.7).midi()
```

Source: `packages/core/controls.mjs`.
