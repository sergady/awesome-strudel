### V

- `v` — alias of `vib`
- `val`
- `vel` — alias of `velocity`
- `velocity`
- `vib`
- `vibmod`
- `vibrato` — alias of `vib`
- `vlpf`
- `vmod` — alias of `vibmod`
- `voice`
- `voices`
- `voicing`
- `voicings`
- `vowel`

## Entries

### val

**Call:** `.val(value)`.

Registered with `uid`, `cps`, and `songPtr`. This checkout does not apply it.

```js
note("c4").s("triangle").val(1).gain(0.2)
```

Source: `packages/core/controls.mjs`.

### velocity

**Call:** `.velocity(…)`. Alias: `vel`.

Sets the velocity from 0 to 1. Is multiplied together with gain.

```js
s("hh*8")
.gain(".4!2 1 .4!2 1 .4 1")
.velocity(".4 1")
```

Source: `packages/core/controls.mjs`.

### vib

**Call:** `.vib(frequency)`. Aliases: `vibrato`, `v`.

Applies a vibrato to the frequency of the oscillator.

```js
note("a e")
.vib("<.5 1 2 4 8 16>")
._scope()
```

```js
// change the modulation depth with ":"
note("a e")
.vib("<.5 1 2 4 8 16>:12")
._scope()
```

Source: `packages/core/controls.mjs`.

### vibmod

**Call:** `.vibmod(depth)`. Alias: `vmod`.

Sets the vibrato depth in semitones. Only has an effect if `vibrato` | `vib` | `v` is is also set

```js
note("a e").vib(4)
.vibmod("<.25 .5 1 2 12>")
._scope()
```

```js
// change the vibrato frequency with ":"
note("a e")
.vibmod("<.25 .5 1 2 12>:8")
._scope()
```

Source: `packages/core/controls.mjs`.

### vlpf

**Call:** `.vlpf(frequency)`.

Not exported. The name appears only as an example of `register`: a custom cutoff that multiplies the frequency by the event's velocity. Run the registration once, then call the new method.

```js
const vlpf = register("vlpf", (freq, pat) => pat.fmap((v) => ({...v, cutoff: freq * (v.velocity ?? 1)})))
s("sawtooth").seg(8).velocity(rand).vlpf(800).gain(0.15)
```

Source: `packages/core/pattern.mjs`.

### voice

**Call:** `.voice(name)`.

Registered as a synth parameter, with no further definition. The browser synth does not read it. Dough voices are the separate `voices` control.

```js
note("c4").s("triangle").voice(0).gain(0.2)
```

Source: `packages/core/controls.mjs`.

### voices

**Call:** `.voices(count)`.

Dough voice-count control, registered beside `group` and `glide`. The source does not say how the count is used.

```js
note("c3 e3 g3").s("sawtooth").voices(4).gain(0.15)
```

Source: `packages/dough/lib.mjs`.

### voicing

**Call:** `.voicing()`.

Turns chord symbols into voicings. You can use the following control params:

- `chord`: Note, followed by chord symbol, e.g. C Am G7 Bb^7
- `dict`: voicing dictionary to use, falls back to default dictionary
- `anchor`: the note that is used to align the chord
- `mode`: how the voicing is aligned to the anchor
  - `below`: top note <= anchor
  - `duck`: top note <= anchor, anchor excluded
  - `above`: bottom note >= anchor
  - `root`: bottom note is the lowest root of the chord >= anchor
  - `oldabove` : old (buggy) behavior of above, kept for legacy reason
  - `oldroot` : old (buggy) behavior of root, kept for legacy reason
- `offset`: whole number that shifts the voicing up or down to the next voicing
- `n`: if set, the voicing is played like a scale. Overshooting numbers will be octaved

All of the above controls are optional, except `chord`.
If you pass a pattern of strings to voicing, they will be interpreted as chords.

```js
n("0 1 2 3").chord("<C Am F G>").voicing()
```

Source: `packages/tonal/voicings.mjs`.

### voicings

**Call:** `.voicings(dictionary)`.

DEPRECATED: still works, but it is recommended you use .voicing instead (without s).
Turns chord symbols into voicings, using the smoothest voice leading possible.
Uses [chord-voicings package](https://github.com/felixroos/chord-voicings#chord-voicings).

```js
stack("<C^7 A7 Dm7 G7>".voicings('lefthand'), "<C3 A2 D3 G2>").note()
```

Source: `packages/tonal/voicings.mjs`.

### vowel

**Call:** `.vowel(vowel)`.

Formant filter to make things sound like vowels.

```js
note("[c2 <eb2 <g2 g1>>]*2").s('sawtooth')
.vowel("<a e i <o u>>")
```

```js
s("bd sd mt ht bd [~ cp] ht lt").vowel("[a|e|i|o|u]")
```

Source: `packages/core/controls.mjs`.
