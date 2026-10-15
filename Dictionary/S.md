### S

- `s`
- `scale`
- `scaleTrans`
- `scaleTranspose`
- `scope`
- `scram`
- `scramble`
- `scrub`
- `seconds`
- `seed`
- `seg`
- `segment`
- `semitone`
- `sequence`
- `set`
- `setcpm`
- `setGainCurve`
- `setMaxPolyphony`
- `shape`
- `shapevol`
- `shrink`
- `shuffle`
- `signal`
- `silence`
- `sinefold`
- `size`
- `slice`
- `slide`
- `slider`
- `slow`
- `slowChunk`
- `slowchunk`
- `smear`
- `soft`
- `someCycles`
- `someCyclesBy`
- `sometimes`
- `sometimesBy`
- `songPtr`
- `sound` — alias of `s`
- `source`
- `sparsity`
- `speak`
- `spectrum`
- `speed`
- `spiral`
- `splice`
- `spread`
- `squiz`
- `src` — alias of `source`
- `stackCenter`
- `stackCentre` — alias of `stackCenter`
- `stackLeft`
- `stackRepeat`
- `stackRight`
- `stepcat`
- `stepsPerOctave`
- `strans`
- `stretch`
- `striate`
- `stut`
- `stutWith`
- `stutwith`
- `sub`
- `superimpose`
- `sus` — alias of `sustain`
- `sustain`
- `sustainpedal`
- `swing`
- `swingBy`
- `sysex`
- `sysexdata`
- `sysexid`
- `sz` — alias of `roomsize`

## Entries

### s

**Call:** `.s(sound)`. Alias: `sound`.

Select a sound / sample by name. When using mininotation, you can also optionally supply 'n' and 'gain' parameters
separated by ':'.

```js
s("bd hh")
```

```js
s("bd:0 bd:1 bd:0:0.3 bd:1:1.4")
```

Source: `packages/core/controls.mjs`.

### scale

**Call:** `.scale(scale)`.

Turns numbers into notes in the scale (zero indexed) or quantizes notes to a scale.

When describing notes via numbers, note that negative numbers can be used to wrap backwards
in the scale as well as sharps or flats to produce notes outside of the scale.

Also sets scale for other scale operations, like {@link Pattern#scaleTranspose}.

A scale consists of a root note (e.g. `c4`, `c`, `f#`, `bb4`) followed by semicolon (':') and then a [scale type](https://github.com/tonaljs/tonal/blob/main/packages/scale-type/data.ts).

The scale name must be written without spaces (because it would be interpreted as a multi-step pattern otherwise).
If your scale name includes spaces, replace them with colons.

The root note defaults to octave 3, if no octave number is given.

```js
n("0 2 4 6 4 2").scale("C:major")
```

```js
n("[0,7] 4 [2,7] 4")
.scale("C:<major minor>/2")
.s("piano")
```

```js
n(rand.range(0,12).segment(8))
.scale("C:ritusen")
.s("piano")
```

```js
n("<[0,7b] [-4# -4] [-2,7##] 4 [0,7] [-4# -4b] [-2,7###] 4b>*4")
.scale("C:<major minor>/2")
.s("piano")
```

```js
note("C1*16").transpose(irand(36)).scale('Cb2 major').scaleTranspose(3)
```

```js
n("[0 0] [1 2] [3 4] [5 6]").scale("C:major:blues")
```

Source: `packages/tonal/tonal.mjs`.

### scaleTrans

**Call:** `.scaleTrans(offset)`. Same as `scaleTranspose`.

Transposes notes inside the scale by the number of steps.
Expected to be called on a Pattern which already has a {@link Pattern#scale}

```js
"-8 [2,4,6]"
.scale('C4 bebop major')
.scaleTranspose("<0 -1 -2 -3 -4 -5 -6 -4>")
.note()
```

Source: `packages/tonal/tonal.mjs`.

### scaleTranspose

**Call:** `.scaleTranspose(offset)`. Aliases: `scaleTrans`, `strans`.

Transposes notes inside the scale by the number of steps.
Expected to be called on a Pattern which already has a {@link Pattern#scale}

```js
"-8 [2,4,6]"
.scale('C4 bebop major')
.scaleTranspose("<0 -1 -2 -3 -4 -5 -6 -4>")
.note()
```

Source: `packages/tonal/tonal.mjs`.

### scope

**Call:** `.scope(config, align, color, thickness, scale, pos, trigger)`. Alias: `tscope`.

Renders an oscilloscope for the time domain of the audio signal.

```js
s("sawtooth")._scope()
```

Source: `packages/webaudio/scope.mjs`.

### scram

**Call:** `.scram(amount)`.

Scrambling of spectral bins. The browser synth does not read this control. It is registered with the other SuperDirt effects, next to `waveloss`.

```js
note("c3").s("sawtooth").scram("<0 .4 .8>").osc().gain(0.15)
```

Source: `packages/core/controls.mjs`.

### scramble

**Call:** `.scramble(…)`.

Slices a pattern into the given number of parts, then plays those parts at random. Similar to `shuffle`,
but parts might be played more than once, or not at all, per cycle.

```js
note("c d e f").sound("piano").scramble(4)
```

```js
seq("c d e f".scramble(4), "g").note().sound("piano")
```

Source: `packages/core/signal.mjs`.

### scrub

**Call:** `.scrub(…)`.

Allows you to scrub an audio file like a tape loop by passing values that represents the position in the audio file
in the optional array syntax ex: "0.5:2", the second value controls the speed of playback

```js
samples('github:switchangel/pad')
s("swpad:0").scrub("{0.1!2 .25@3 0.7!2 <0.8:1.5>}%8")
```

```js
samples('github:yaxu/clean-breaks/main');
s("amen/4").fit().scrub("{0@3 0@2 4@3}%8".div(16))
```

Source: `packages/core/controls.mjs`.

### seconds

**Call:** `.seconds(count)`.

Registered with `hours`, `minutes`, and `songPtr` as clock metadata. This checkout does not apply it.

```js
note("c4").s("triangle").seconds(0).gain(0.2)
```

Source: `packages/core/controls.mjs`.

### seed

**Call:** `.seed(n)`.

Change the seed for random signals. Normally, random signals depend on time,
so two patterns at the same time will have the same random values. Specifying
a new seed changes the signal output by `rand`. This also affects other functions
that use randomness, like `shuffle` and `sometimes`.

```js
$: s("hh*4").degrade();
$: s("bd*4").degrade().seed(1); // Will degrade different events from the hi-hat
```

Source: `packages/core/signal.mjs`.

### seg

**Call:** `.seg(segments)`. Same as `segment`.

Samples the pattern at a rate of n events per cycle. Useful for turning a continuous pattern into a discrete one.

```js
note(saw.range(40,52).segment(24))
```

Source: `packages/core/pattern.mjs`.

### segment

**Call:** `.segment(segments)`. Alias: `seg`.

Samples the pattern at a rate of n events per cycle. Useful for turning a continuous pattern into a discrete one.

```js
note(saw.range(40,52).segment(24))
```

Source: `packages/core/pattern.mjs`.

### semitone

**Call:** `.semitone(steps)`.

Registered next to `slide`. The source asks whether it is a detune and does not wire it to the browser synth. Pitch shift in the browser is `transpose`.

```js
note("c4 e4 g4").s("triangle").semitone(1).gain(0.2)
```

Source: `packages/core/controls.mjs`.

### sequence

**Call:** `sequence`.

See `fastcat`

Source: `packages/core/pattern.mjs`.

### set

**Call:** `.set(pat)`.

When called on a pattern `a`, with a input pattern `b` (`a.set(b)`),
combines `a` and `b` such that anything defined in `b`
and anything defined in `a` that is *not* defined in `b`
will be in the resulting pattern.

The structure is maintained from `a`,
because the default pattern alignment is `in`,
see the section on `Pattern Alignment`
in the technical manual in the docs

This is the inverse of `keep`

See examples below

```js
// because input pattern has `s` set,
// it overrides the "sine" declared earlier
note("c a f e").s("sine").set(s("triangle"))
```

Source: `packages/core/pattern.mjs`.

### setcpm

**Call:** `setcpm(cpm)`.

Changes the global tempo to the given cycles per minute

```js
setcpm(140/4) // =140 bpm in 4/4
$: s("bd*4,[- sd]*2").bank('tr707')
```

Source: `packages/core/repl.mjs`.

### setGainCurve

**Call:** `setGainCurve(function)`.

Apply a function to all gains provided in patterns. Can be used to rescale gain to be
quadratic, exponential, etc. rather than linear

```js
setGainCurve((x) => x * x) // quadratic gain
s("bd*4").gain(0.5) // equivalent to 0.25 gain normally
```

Source: `packages/superdough/superdough.mjs`.

### setMaxPolyphony

**Call:** `setMaxPolyphony(…)`.

Set the max polyphony. If notes are ringing out via `release` then they will
start to die out in first-in-first-out order once the max polyphony has been hit

```js
setMaxPolyphony(4)
n(irand(24).seg(8)).scale("C#3:minor").room(1).release(4).gain(0.5)
```

Source: `packages/superdough/superdough.mjs`.

### shape

**Call:** `.shape(distortion)`.

(Deprecated) Wave shaping distortion. WARNING: can suddenly get unpredictably loud.
Please use distort instead, which has a more predictable response curve
second option in optional array syntax (ex: ".9:.5") applies a postgain to the output

```js
s("bd sd [~ bd] sd,hh*8").shape("<0 .2 .4 .6 .8>")
```

Source: `packages/core/controls.mjs`.

### shapevol

**Call:** `.shapevol(gain)`.

Gain after the waveshaper. `shape` is the amount of shaping, and this is the level of the shaped signal. The default is 1.

```js
note("c3").s("sawtooth").shape(0.6).shapevol("<0.2 1>").gain(0.15)
```

Source: `packages/core/controls.mjs`.

### shrink

**Call:** `.shrink()`.

*Experimental*

Progressively shrinks the pattern by 'n' steps until there's nothing left, or if a second value is given (using mininotation list syntax with `:`),
that number of times.
A positive number will progressively drop steps from the start of a pattern, and a negative number from the end.



"tha dhi thom nam".shrink("1").sound()
.bank("mridangam")

"tha dhi thom nam".shrink("-1").sound()
.bank("mridangam")

"tha dhi thom nam".shrink("1 -1").sound().bank("mridangam").pace(4)

note("0 1 2 3 4 5 6 7".scale("C:ritusen")).sound("folkharp")
.shrink("1 -1").pace(8)

Source: `packages/core/pattern.mjs`.

### shuffle

**Call:** `.shuffle(…)`.

Slices a pattern into the given number of parts, then plays those parts in random order.
Each part will be played exactly once per cycle.

```js
note("c d e f").sound("piano").shuffle(4)
```

```js
seq("c d e f".shuffle(4), "g").note().sound("piano")
```

Source: `packages/core/signal.mjs`.

### signal

**Call:** `signal(func)`.

Creates a signal given by the input function

```js
// sawtooth signal definition
signal(t=>t%1).segment(16).range(30,40).note()
```

```js
signal(t=>Math.pow(t,2)%1).range(40, 60).add(5).segment(16)
.off(0, x=>x.add(7))
.note()
.s("gm_electric_guitar_jazz,gm_epiano")
  .gain(1.7)
.pianoroll()
```

Source: `packages/core/signal.mjs`.

### silence

**Call:** `silence`.

Does absolutely nothing..

```js
silence // "~"
```

Source: `packages/core/pattern.mjs`.

### sinefold

**Call:** `.sinefold(distortion, volume)`.

Wavefolding distortion composed with sinusoid

Source: `packages/core/pattern.mjs`.

### size

**Call:** `.size(size)`. Same as `roomsize`.

Sets the room size of the reverb, see `room`.
When this property is changed, the reverb will be recaculated, so only change this sparsely..

```js
s("bd sd [~ bd] sd").room(.8).rsize(1)
```

```js
s("bd sd [~ bd] sd").room(.8).rsize(4)
```

Source: `packages/core/controls.mjs`.

### slice

**Call:** `.slice(…)`.

Chops samples into the given number of slices, triggering those slices with a given pattern of slice numbers.
Instead of a number, it also accepts a list of numbers from 0 to 1 to slice at specific points.

```js
samples('github:tidalcycles/dirt-samples')
s("breaks165").slice(8, "0 1 <2 2*2> 3 [4 0] 5 6 7".every(3, rev)).slow(0.75)
```

```js
samples('github:tidalcycles/dirt-samples')
s("breaks125").fit().slice([0,.25,.5,.75], "0 1 1 <2 3>")
```

Source: `packages/core/pattern.mjs`.

### slide

**Call:** `.slide(amount)`.

Pitch glide of a ZZFX sound. Positive values sweep the frequency while the note plays. `deltaSlide` then speeds that glide up or down. The same name is also registered as an undocumented synth parameter.

```js
s("z_sine").note("c3").slide("<0 .3 1>").gain(0.2)
```

Source: `packages/core/controls.mjs`.

### slider

**Call:** `slider(value, min, max, step)`.

Displays a slider widget to allow the user manipulate a value

Source: `packages/codemirror/slider.mjs`.

### slow

**Call:** `.slow(factor)`. Alias: `sparsity`.

Slow down a pattern over the given number of cycles. Like the "/" operator in mini notation.

```js
s("bd hh sd hh").slow(2) // s("[bd hh sd hh]/2")
```

Source: `packages/core/pattern.mjs`.

### slowChunk

**Call:** `.slowChunk()`. Same as `chunk`.

Divides a pattern into a given number of parts, then cycles through those parts in turn, applying the given function to each part in turn (one part per cycle).

```js
"0 1 2 3".chunk(4, x=>x.add(7))
.scale("A:minor").note()
```

Source: `packages/core/pattern.mjs`.

### slowchunk

**Call:** `.slowchunk()`. Same as `chunk`.

Divides a pattern into a given number of parts, then cycles through those parts in turn, applying the given function to each part in turn (one part per cycle).

```js
"0 1 2 3".chunk(4, x=>x.add(7))
.scale("A:minor").note()
```

Source: `packages/core/pattern.mjs`.

### smear

**Call:** `.smear(amount)`.

Two registrations share this name. In `controls.mjs` it is a SuperDirt spectral smear, which the browser synth does not apply. In `draw/animate.mjs` it is a drawing parameter next to `x`, `y`, `w`, and `h`. Whichever package is loaded later owns the method.

```js
note("c3").s("sawtooth").smear("<0 .5 1>").osc().gain(0.15)
```

Source: `packages/core/controls.mjs`.

### soft

**Call:** `.soft(distortion, volume)`.

Soft-clipping distortion

Source: `packages/core/pattern.mjs`.

### someCycles

**Call:** `.someCycles(…)`.

Shorthand for `.someCyclesBy(0.5, fn)`

```js
s("bd,hh*8").someCycles(x=>x.speed("0.5"))
```

Source: `packages/core/signal.mjs`.

### someCyclesBy

**Call:** `.someCyclesBy(probability, function)`.

Randomly applies the given function by the given probability on a cycle by cycle basis.
Similar to `sometimesBy`

```js
s("bd,hh*8").someCyclesBy(.3, x=>x.speed("0.5"))
```

Source: `packages/core/signal.mjs`.

### sometimes

**Call:** `.sometimes(function)`.

Applies the given function with a 50% chance

```js
s("hh*8").sometimes(x=>x.speed("0.5"))
```

Source: `packages/core/signal.mjs`.

### sometimesBy

**Call:** `.sometimesBy(probability, function)`.

Randomly applies the given function by the given probability.
Similar to `someCyclesBy`

```js
s("hh*8").sometimesBy(.4, x=>x.speed("0.5"))
```

Source: `packages/core/signal.mjs`.

### songPtr

**Call:** `.songPtr(position)`.

Registered with the clock-metadata controls. This checkout does not apply it.

```js
note("c4").s("triangle").songPtr(0).gain(0.2)
```

Source: `packages/core/controls.mjs`.

### source

**Call:** `.source(getSource)`. Alias: `src`.

Define a custom webaudio node to use as a sound source.

Source: `packages/core/controls.mjs`.

### sparsity

**Call:** `.sparsity(factor)`. Same as `slow`.

Slow down a pattern over the given number of cycles. Like the "/" operator in mini notation.

```js
s("bd hh sd hh").slow(2) // s("[bd hh sd hh]/2")
```

Source: `packages/core/pattern.mjs`.

### speak

**Call:** `.speak(lang, voice)`.

Speaks each event value with the browser speech synthesizer. `lang` is a language tag such as `en`. `voice` is an index into the voices for that language, or a voice name.

```js
"one two three four".speak("en", 0)
```

Source: `packages/core/speak.mjs`.

### spectrum

**Call:** `.spectrum(config, thickness, speed, min, max)`.

Renders a spectrum analyzer for the incoming audio signal.

```js
n("<0 4 <2 3> 1>*3")
.off(1/8, add(n(5)))
.off(1/5, add(n(7)))
.scale("d3:minor:pentatonic")
.s('sine')
.dec(.3).room(.5)
._spectrum()
```

Source: `packages/webaudio/spectrum.mjs`.

### speed

**Call:** `.speed(speed)`.

Changes the speed of sample playback, i.e. a cheap way of changing pitch.

```js
s("bd*6").speed("1 2 4 1 -2 -4")
```

```js
speed("1 1.5*2 [2 1.1]").s("piano").clip(1)
```

Source: `packages/core/controls.mjs`.

### spiral

**Call:** `.spiral(options, stretch, size, thickness, cap, inset, playheadColor, playheadLength, playheadThickness, padding, steady, activeColor, inactiveColor, colorizeInactive, fade, logSpiral)`.

Displays a spiral visual.

```js
note("c2 a2 eb2")
.euclid(5,8)
.s('sawtooth')
.lpenv(4).lpf(300)
._spiral({ steady: .96 })
```

Source: `packages/draw/spiral.mjs`.

### splice

**Call:** `.splice(…)`.

Works the same as slice, but changes the playback speed of each slice to match the duration of its step.

```js
samples('github:tidalcycles/dirt-samples')
s("breaks165")
.splice(8,  "0 1 [2 3 0]@2 3 0@2 7")
```

Source: `packages/core/pattern.mjs`.

### spread

**Call:** `.spread(spread)`.

Set the stereo pan spread for supported oscillators

```js
note("d f a a# a d3").fast(2).s("supersaw").spread("<0 .3 1>")
```

Source: `packages/core/controls.mjs`.

### squiz

**Call:** `.squiz(squiz)`.

Made by Calum Gunn. Reminiscent of some weird mixture of filter, ring-modulator and pitch-shifter. The SuperCollider manual defines Squiz as:

"A simplistic pitch-raising algorithm. It's not meant to sound natural; its sound is reminiscent of some weird mixture of filter, ring-modulator and pitch-shifter, depending on the input. The algorithm works by cutting the signal into fragments (delimited by upwards-going zero-crossings) and squeezing those fragments in the time domain (i.e. simply playing them back faster than they came in), leaving silences inbetween. All the parameters apart from memlen can be modulated."

```js
squiz("2 4/2 6 [8 16]").s("bd").osc()
```

Source: `packages/core/controls.mjs`.

### stackCenter

**Call:** `.stackCenter(…)`. Alias: `stackCentre`.

The input patterns are aligned to the right, with silence padded to the shorter pattern(s) in the initial steps if there's a stepcount disparity. See also `stackLeft` and `stackRight`

```js
stackCenter("0 1 2 3", "3 4", "[4 5 6] 7 8 9 10").scale("c:minor").note()
```

```js
// chainable
"0 1 2 3".stackCenter("3 4", "[4 5 6] 7 8 9 10").scale("c:minor").note()
```

Source: `packages/core/pattern.mjs`.

### stackLeft

**Call:** `.stackLeft(…)`.

The input patterns are aligned to the left, with silence padded to the shorter pattern(s) in the final steps if there's a stepcount disparity. See also `stackRight` and `stackCenter/stackCentre`

```js
stackLeft("0 1 2 3", "3 4", "[4 5 6] 7 8 9 10").scale("c:minor").note()
```

```js
// chainable
"0 1 2 3".stackLeft("3 4", "[4 5 6] 7 8 9 10").scale("c:minor").note()
```

Source: `packages/core/pattern.mjs`.

### stackRepeat

**Call:** `.stackRepeat(…)`.

Shorthand for `pm(patterns).pace(m)` where m is the max step count in the input patterns

```js
stackRepeat("0 1 2 3", "3 4", "[4 5 6] 7 8 9 10").scale("c:minor").note()
```

```js
// chainable
"0 1 2 3".stackRepeat("3 4", "[4 5 6] 7 8 9 10").scale("c:minor").note()
```

Source: `packages/core/pattern.mjs`.

### stackRight

**Call:** `.stackRight(…)`.

The input patterns are aligned to the right, with silence padded to the shorter pattern(s) in the initial steps if there's a stepcount disparity. See also `stackLeft` and `stackCenter/stackCentre`

```js
stackRight("0 1 2 3", "3 4", "[4 5 6] 7 8 9 10").scale("c:minor").note()
```

```js
// chainable
"0 1 2 3".stackRight("3 4", "[4 5 6] 7 8 9 10").scale("c:minor").note()
```

Source: `packages/core/pattern.mjs`.

### stepcat

**Call:** `stepcat(…)`. Aliases: `timeCat`, `timecat`.

'Concatenates' patterns like `fastcat`, but proportional to a number of steps per cycle.
The steps can either be inferred from the pattern, or provided as a [length, pattern] pair.
Has the alias `timecat`.

```js
stepcat([3,"e3"],[1, "g3"]).note()
// the same as "e3@3 g3".note()
```

```js
stepcat("bd sd cp","hh hh").sound()
// the same as "bd sd cp hh hh".sound()
```

Source: `packages/core/pattern.mjs`.

### stepsPerOctave

**Call:** `.stepsPerOctave(count)`.

Registered control. The source says it was not found in the Tidal documentation, and this checkout does not apply it.

```js
n("0 2 4 6").scale("C:major").stepsPerOctave(12).s("triangle").gain(0.2)
```

Source: `packages/core/controls.mjs`.

### strans

**Call:** `.strans(offset)`. Same as `scaleTranspose`.

Transposes notes inside the scale by the number of steps.
Expected to be called on a Pattern which already has a {@link Pattern#scale}

```js
"-8 [2,4,6]"
.scale('C4 bebop major')
.scaleTranspose("<0 -1 -2 -3 -4 -5 -6 -4>")
.note()
```

Source: `packages/tonal/tonal.mjs`.

### stretch

**Call:** `.stretch(factor)`.

Changes the pitch of the sample without changing its speed.
The frequencies are multiplied by (factor + 1) for positive numbers
and by max(factor / 4 + 1, 0) for negative numbers.
So tuning up by octaves can be done with 1, 3, 7, ...
and tuning down by octaves with -2, -3, -3.5...

```js
s("gm_flute").stretch("<2 1 0 -2>")
```

Source: `packages/core/controls.mjs`.

### striate

**Call:** `.striate(…)`.

Cuts each sample into the given number of parts, triggering progressive portions of each sample at each loop.

```js
s("numbers:0 numbers:1 numbers:2").striate(6).slow(3)
```

Source: `packages/core/pattern.mjs`.

### stut

**Call:** `.stut(times, feedback, time)`.

Deprecated. Like echo, but the last 2 parameters are flipped.

```js
s("bd sd").stut(3, .8, 1/6)
```

Source: `packages/core/pattern.mjs`.

### stutWith

**Call:** `.stutWith(times, time, func)`. Same as `echoWith`.

Superimpose and offset multiple times, applying the given function each time.

```js
"<0 [2 4]>"
.echoWith(4, 1/8, (p,n) => p.add(n*2))
.scale("C:minor").note()
```

Source: `packages/core/pattern.mjs`.

### stutwith

**Call:** `.stutwith(times, time, func)`. Same as `echoWith`.

Superimpose and offset multiple times, applying the given function each time.

```js
"<0 [2 4]>"
.echoWith(4, 1/8, (p,n) => p.add(n*2))
.scale("C:minor").note()
```

Source: `packages/core/pattern.mjs`.

### sub

**Call:** `.sub(…)`.

Like add, but the given numbers are subtracted.

```js
n("0 2 4".sub("<0 1 2 3>")).scale("C4:minor")
// See add for more information.
```

Source: `packages/core/pattern.mjs`.

### superimpose

**Call:** `.superimpose(…)`.

Superimposes the result of the given function(s) on top of the original pattern:

```js
"<0 2 4 6 ~ 4 ~ 2 0!3 ~!5>*8"
  .superimpose(x=>x.add(2))
  .scale('C minor').note()
```

Source: `packages/core/pattern.mjs`.

### sustain

**Call:** `.sustain(gain)`. Alias: `sus`.

Amplitude envelope sustain level: The level which is reached after attack / decay, being sustained until the offset.

```js
note("c3 e3 f3 g3").decay(.2).sustain("<0 .1 .4 .6 1>")
```

Source: `packages/core/controls.mjs`.

### sustainpedal

**Call:** `.sustainpedal(down)`.

MIDI sustain-pedal control, registered next to `expression`. The MIDI output in this checkout does not send it.

```js
note("c4 e4 g4 c5").sustainpedal("<0 1>").midi()
```

Source: `packages/core/controls.mjs`.

### swing

**Call:** `.swing()`.

Shorthand for swingBy with 1/3:



s("hh*8").swing(4)
// s("hh*8").swingBy(1/3, 4)

Source: `packages/core/pattern.mjs`.

### swingBy

**Call:** `.swingBy()`.

The function `swingBy x n` breaks each cycle into `n` slices, and then delays events in the second half of each slice by the amount `x`, which is relative to the size of the (half) slice. So if `x` is 0 it does nothing, `0.5` delays for half the note duration, and 1 will wrap around to doing nothing again. The end result is a shuffle or swing-like rhythm




s("hh*8").swingBy(1/3, 4)

Source: `packages/core/pattern.mjs`.

### sysex

**Call:** `.sysex(id, data)`.

MIDI sysex: Sends a MIDI sysex message.

```js
note("c4").sysex(["0x77", "0x01:0x02:0x03:0x04"]).midichan(1).midi()
```

Source: `packages/core/controls.mjs`.

### sysexdata

**Call:** `.sysexdata(data)`.

MIDI sysex data: Sends a MIDI sysex message.

```js
note("c4").sysexid("0x77").sysexdata("0x01:0x02:0x03:0x04").midichan(1).midi()
```

Source: `packages/core/controls.mjs`.

### sysexid

**Call:** `.sysexid(id)`.

MIDI sysex ID: Sends a MIDI sysex identifier message.

```js
note("c4").sysexid("0x77").sysexdata("0x01:0x02:0x03:0x04").midichan(1).midi()
```

Source: `packages/core/controls.mjs`.
