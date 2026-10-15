### N

- `n`
- `ne`
- `net`
- `never`
- `noise`
- `note`
- `nrpnn`
- `nrpv`
- `nudge`

## Entries

### n

**Call:** `.n(value)`.

Selects the given index:
 - for samples, it picks the sample by index, with wrap around
 - for scales, it picks the scale degree
 - for voicings, it picks the voice index

```js
s("bd sd [~ bd] sd,hh*6").n("<0 1>")
```

Source: `packages/core/controls.mjs`.

### ne

**Call:** `ne(a, b)`.

performs a != b

Source: `packages/core/pattern.mjs`.

### net

**Call:** `net(a, b)`.

performs a !== b (strictly not equal)

Source: `packages/core/pattern.mjs`.

### never

**Call:** `.never(…)`.

Shorthand for `.sometimesBy(0, fn)` (never calls fn)

```js
s("hh*8").never(x=>x.speed("0.5"))
```

Source: `packages/core/signal.mjs`.

### noise

**Call:** `.noise(wet)`.

Adds pink noise to the mix

```js
sound("<white pink brown>/2")
```

Source: `packages/core/controls.mjs`.

### note

**Call:** `.note(…)`.

Plays the given note name or midi number. A note name consists of

- a letter (a-g or A-G)
- optional accidentals (b or #)
- optional (possibly negative) octave number (0-9). Defaults to 3

Examples of valid note names: `c`, `bb`, `Bb`, `f#`, `c3`, `A4`, `Eb2`, `c#5`

You can also use midi numbers instead of note names, where 69 is mapped to A4 440Hz in 12EDO.

```js
note("c a f e")
```

```js
note("c4 a4 f4 e4")
```

```js
note("60 69 65 64")
```

```js
note("fbb1 a#0 cbbb-1 e##-2").sound("saw")
```

Source: `packages/core/controls.mjs`.

### nrpnn

**Call:** `.nrpnn(nrpnn)`.

MIDI NRPN non-registered parameter number: Sends a MIDI NRPN non-registered parameter number message.

```js
note("c4").nrpnn("1:8").nrpv("123").midichan(1).midi()
```

Source: `packages/core/controls.mjs`.

### nrpv

**Call:** `.nrpv(nrpv)`.

MIDI NRPN non-registered parameter value: Sends a MIDI NRPN non-registered parameter value message.

```js
note("c4").nrpnn("1:8").nrpv("123").midichan(1).midi()
```

Source: `packages/core/controls.mjs`.

### nudge

**Call:** `.nudge(seconds)`.

Delays the outgoing OSC message by this many seconds. The source says it cannot be negative beyond the latency, which is why it is not the same control as `early` or `late`. The browser synth does not read it.

```js
s("bd*4").nudge(0.05).osc()
```

Source: `packages/core/controls.mjs`.
