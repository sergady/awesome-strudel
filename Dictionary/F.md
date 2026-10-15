### F

- `fadeInTime`
- `fadeOutTime` — alias of `fadeTime`
- `fadeTime`
- `fanchor`
- `fast`
- `fastChunk`
- `fastchunk`
- `fastGap`
- `fastgap`
- `fft`
- `filter`
- `filterWhen`
- `firstOf`
- `fit`
- `floor`
- `flux`
- `fluxBy`
- `fluxby`
- `fm`
- `fmatt` — alias of `fmattack`
- `fmattack`
- `fmdec` — alias of `fmdecay`
- `fmdecay`
- `fme` — alias of `fmenv`
- `fmenv`
- `fmh`
- `fmi`
- `fmrel` — alias of `fmrelease`
- `fmrelease`
- `fmsus` — alias of `fmsustain`
- `fmsustain`
- `fmwave`
- `focus`
- `focusSpan`
- `focusspan`
- `fold`
- `frameRate`
- `frames`
- `freeze`
- `freq`
- `fromBipolar`
- `fscope`
- `fshift`
- `fshiftnote`
- `fshiftphase`
- `ftrans`
- `fTrans`
- `ftranspose`
- `fTranspose`
- `ftype`
- `FX`
- `FXrelease`

## Entries

### fadeInTime

**Call:** `.fadeInTime(time)`.

Registered beside `fadeTime`, the fade-out of a chopped or sliced grain. This is the matching fade-in control. The source documents `fadeTime` only, and the browser synth does not read `fadeInTime`.

```js
s("bd*4").begin(0.2).fadeInTime("<0 .2 .5>")
```

Source: `packages/core/controls.mjs`.

### fadeTime

**Call:** `.fadeTime(time)`. Alias: `fadeOutTime`.

Used when using `begin`/`end` or `chop`/`striate` and friends, to change the fade out time of the 'grain' envelope.

```js
s("oh*4").end(.1).fadeTime("<0 .2 .4 .8>").osc()
```

Source: `packages/core/controls.mjs`.

### fanchor

**Call:** `.fanchor(center)`.

controls the center of the filter envelope. 0 is unipolar positive, .5 is bipolar, 1 is unipolar negative

```js
note("{f g g c d a a#}%8").s("sawtooth").lpf("{1000}%2")
.lpenv(8).fanchor("<0 .5 1>")
```

Source: `packages/core/controls.mjs`.

### fast

**Call:** `.fast(factor)`. Alias: `density`.

Speed up a pattern by the given factor. Used by "*" in mini notation.

```js
s("bd hh sd hh").fast(2) // s("[bd hh sd hh]*2")
```

Source: `packages/core/pattern.mjs`.

### fastChunk

**Call:** `.fastChunk(…)`. Alias: `fastchunk`.

Like `chunk`, but the cycles of the source pattern aren't repeated
for each set of chunks.

```js
"<0 8> 1 2 3 4 5 6 7"
.scale("C2:major").note()
.fastChunk(4, x => x.color('red')).slow(2)
```

Source: `packages/core/pattern.mjs`.

### fastchunk

**Call:** `.fastchunk()`. Same as `fastChunk`.

Like `chunk`, but the cycles of the source pattern aren't repeated
for each set of chunks.

```js
"<0 8> 1 2 3 4 5 6 7"
.scale("C2:major").note()
.fastChunk(4, x => x.color('red')).slow(2)
```

Source: `packages/core/pattern.mjs`.

### fastGap

**Call:** `.fastGap(…)`. Alias: `fastgap`.

speeds up a pattern like fast, but rather than it playing multiple times as fast would it instead leaves a gap in the remaining space of the cycle. For example, the following will play the sound pattern "bd sn" only once but compressed into the first half of the cycle, i.e. twice as fast.

```js
s("bd sd").fastGap(2)
```

Source: `packages/core/pattern.mjs`.

### fastgap

**Call:** `.fastgap()`. Same as `fastGap`.

speeds up a pattern like fast, but rather than it playing multiple times as fast would it instead leaves a gap in the remaining space of the cycle. For example, the following will play the sound pattern "bd sn" only once but compressed into the first half of the cycle, i.e. twice as fast.

```js
s("bd sd").fastGap(2)
```

Source: `packages/core/pattern.mjs`.

### fft

**Call:** `.fft(size)`.

Exponent for the analyser window used by `analyze`. The window length is `2 ** (fft + 5)`. The default is 8, which is 8192 samples. Values run from 0 to 10.

```js
note("c3 e3 g3").s("sawtooth").analyze(1).fft("<5 8 10>").gain(0.15)
```

Source: `packages/core/controls.mjs`.

### filter

**Call:** `.filter(test)`.

Filters haps using the given function

```js
s("hh!7 oh").filter(hap => hap.value.s === 'hh')
```

Source: `packages/core/pattern.mjs`.

### filterWhen

**Call:** `.filterWhen(test)`.

Filters haps by their begin time

```js
oneCycle: s("bd*4").filterWhen((t) => t < 1)
```

Source: `packages/core/pattern.mjs`.

### firstOf

**Call:** `.firstOf(n, func)`.

Applies the given function every n cycles, starting from the first cycle.

```js
note("c3 d3 e3 g3").firstOf(4, x=>x.rev())
```

Source: `packages/core/pattern.mjs`.

### fit

**Call:** `.fit()`.

Makes the sample fit its event duration. Good for rhythmical loops like drum breaks.
Similar to `loopAt`.

```js
samples({ rhodes: 'https://cdn.freesound.org/previews/132/132051_316502-lq.mp3' })
s("rhodes/2").fit()
```

Source: `packages/core/pattern.mjs`.

### floor

**Call:** `.floor()`.

Assumes a numerical pattern. Returns a new pattern with all values set to
their mathematical floor. E.g. `3.7` replaced with to `3`, and `-4.2`
replaced with `-5`.

```js
note("42 42.1 42.5 43".floor())
```

Source: `packages/core/pattern.mjs`.

### flux

**Call:** `.flux()`. Same as `juxFlip`.

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

### fluxBy

**Call:** `.fluxBy()`. Same as `juxFlipBy`.

Like juxBy, except it flips the ears each cycle.

```js
s("bd lt [~ ht] mt cp ~ bd hh").juxFlipBy(".8", rev)
```

Source: `packages/core/pattern.mjs`.

### fluxby

**Call:** `.fluxby()`. Same as `juxFlipBy`.

Like juxBy, except it flips the ears each cycle.

```js
s("bd lt [~ ht] mt cp ~ bd hh").juxFlipBy(".8", rev)
```

Source: `packages/core/pattern.mjs`.

### fm

**Call:** `.fm(brightness)`. Alias: `fmi`.

Sets the Frequency Modulation of the synth.
Controls the modulation index, which defines the brightness of the sound.

A number may be added afterwards to control the modulation index of
any of the 8 individual FMs (e.g. `fm3`). Also, FMs may be routed into
each other with matrix commands like `fm13`, which would send `fm1` back into
`fm3`

```js
note("c e g b g e")
.fm("<0 1 2 8 32>")
._scope()
```

```js
s("sine").note("F1").seg(8)
 .fm(4).fm2(rand.mul(4)).fm3(saw.mul(8).slow(8))
 .fmh(1.06).fmh2(10).fmh3(0.1)
```

Source: `packages/core/controls.mjs`.

### fmattack

**Call:** `.fmattack(time)`. Alias: `fmatt`.

Attack time for the FM envelope: time it takes to reach maximum modulation

A number may be added afterwards to control the attack of the envelope of
any of the 8 individual FMs (e.g. `fmatt5`)

```js
note("c e g b g e")
.fm(4)
.fmattack("<0 .05 .1 .2>")
._scope()
```

Source: `packages/core/controls.mjs`.

### fmdecay

**Call:** `.fmdecay(time)`. Alias: `fmdec`.

Decay time for the FM envelope: seconds until the sustain level is reached after the attack phase.

A number may be added afterwards to control the decay of the envelope of
any of the 8 individual FMs (e.g. `fmdec6`)

```js
note("c e g b g e")
.fm(4)
.fmdecay("<.01 .05 .1 .2>")
.fmsustain(.4)
._scope()
```

Source: `packages/core/controls.mjs`.

### fmenv

**Call:** `.fmenv(type)`. Alias: `fme`.

Ramp type of fm envelope. Exp might be a bit broken..

A number may be added afterwards to control the envelope of
any of the 8 individual FMs (e.g. `fmenv4`)

```js
note("c e g b g e")
.fm(4)
.fmdecay(.2)
.fmsustain(0)
.fmenv("<exp lin>")
._scope()
```

Source: `packages/core/controls.mjs`.

### fmh

**Call:** `.fmh(harmonicity)`.

Sets the Frequency Modulation Harmonicity Ratio.
Controls the timbre of the sound.
Whole numbers and simple ratios sound more natural,
while decimal numbers and complex ratios sound metallic.

A number may be added afterwards to control the harmonicity of
any of the 8 individual FMs (e.g. `fmh2`)

```js
note("c e g b g e")
.fm(4)
.fmh("<1 2 1.5 1.61>")
._scope()
```

Source: `packages/core/controls.mjs`.

### fmi

**Call:** `.fmi(brightness)`. Same as `fm`.

Sets the Frequency Modulation of the synth.
Controls the modulation index, which defines the brightness of the sound.

A number may be added afterwards to control the modulation index of
any of the 8 individual FMs (e.g. `fm3`). Also, FMs may be routed into
each other with matrix commands like `fm13`, which would send `fm1` back into
`fm3`

```js
note("c e g b g e")
.fm("<0 1 2 8 32>")
._scope()
```

```js
s("sine").note("F1").seg(8)
 .fm(4).fm2(rand.mul(4)).fm3(saw.mul(8).slow(8))
 .fmh(1.06).fmh2(10).fmh3(0.1)
```

Source: `packages/core/controls.mjs`.

### fmrelease

**Call:** `.fmrelease(time)`. Alias: `fmrel`.

Release time for the FM envelope: how much modulation is applied after the note is released

A number may be added afterwards to control the release of the envelope of
any of the 8 individual FMs (e.g. `fmrel8`)

Source: `packages/core/controls.mjs`.

### fmsustain

**Call:** `.fmsustain(level)`. Alias: `fmsus`.

Sustain level for the FM envelope: how much modulation is applied after the decay phase

A number may be added afterwards to control the sustain of the envelope of
any of the 8 individual FMs (e.g. `fmsus7`)

```js
note("c e g b g e")
.fm(4)
.fmdecay(.1)
.fmsustain("<1 .75 .5 0>")
._scope()
```

Source: `packages/core/controls.mjs`.

### fmwave

**Call:** `.fmwave(wave)`.

Waveform of the fm modulator

A number may be added afterwards to control the waveform
any of the 8 individual FMs (e.g. `fmwave6`)

```js
n("0 1 2 3".fast(4)).scale("d:minor").s("sine").fmwave("<sine square sawtooth crackle>").fm(4).fmh(2.01)
```

```js
n("0 1 2 3".fast(4)).chord("<Dm Am F G>").voicing().s("sawtooth").fmwave("brown").fm(.6)
```

Source: `packages/core/controls.mjs`.

### focus

**Call:** `.focus(begin, end)`.

Fits the whole pattern between two cycle positions and does not leave the rest of the cycle empty. The focused span can be longer than one cycle, unlike `compress`.

```js
s("bd hh sd hh").focus(1/4, 3/4)
```

Source: `packages/core/pattern.mjs`.

### focusSpan

**Call:** `.focusSpan(span)`.

Same function as `focus`, reading `begin` and `end` from one value. `focusspan` is the same function.

```js
s("bd hh sd hh").focus(0.25, 0.75)
```

Source: `packages/core/pattern.mjs`.

### focusspan

**Call:** `.focusspan(span)`.

Same function as `focusSpan`.

```js
s("bd hh sd hh").focusspan({begin: 0.25, end: 0.75})
```

Source: `packages/core/pattern.mjs`.

### fold

**Call:** `.fold(distortion, volume)`.

Wavefolding distortion

Source: `packages/core/pattern.mjs`.

### frameRate

**Call:** `.frameRate(rate)`.

Registered with the playback-metadata controls (`frames`, `hours`, `minutes`, `seconds`, `songPtr`). This checkout does not apply it.

```js
note("c4").s("triangle").frameRate(30).gain(0.2)
```

Source: `packages/core/controls.mjs`.

### frames

**Call:** `.frames(count)`.

Registered with `frameRate` and the clock-metadata controls. This checkout does not apply it.

```js
note("c4").s("triangle").frames(16).gain(0.2)
```

Source: `packages/core/controls.mjs`.

### freeze

**Call:** `.freeze(amount)`.

Spectral freeze, holding the current spectrum. The browser synth does not read this control. It is registered with the other SuperDirt effects, next to `waveloss`.

```js
note("c3").s("sawtooth").freeze("<0 1>").osc().gain(0.15)
```

Source: `packages/core/controls.mjs`.

### freq

**Call:** `.freq(frequency)`.

Set frequency of sound.

```js
freq("220 110 440 110").s("superzow").osc()
```

```js
freq("110".mul.out(".5 1.5 .6 [2 3]")).s("superzow").osc()
```

Source: `packages/core/controls.mjs`.

### fromBipolar

**Call:** `.fromBipolar()`.

Assumes a numerical pattern, containing bipolar values in the range -1 .. 1
Returns a new pattern with values scaled to the unipolar range 0 .. 1

Source: `packages/core/pattern.mjs`.

### fscope

**Call:** `.fscope(color, scale, pos, lean, min, max)`.

Renders an oscilloscope for the frequency domain of the audio signal.

```js
s("sawtooth").fscope()
```

Source: `packages/webaudio/scope.mjs`.

### fshift

**Call:** `.fshift(amount)`.

Frequency shift. The browser synth does not read this control. It is registered with the other SuperDirt effects, next to `waveloss`.

```js
note("c3").s("sawtooth").fshift("<0 20 80>").osc().gain(0.15)
```

Source: `packages/core/controls.mjs`.

### fshiftnote

**Call:** `.fshiftnote(steps)`.

Frequency shift in note steps, beside `fshift`. The browser synth does not read this control. It is registered with the other SuperDirt effects, next to `waveloss`.

```js
note("c3").s("sawtooth").fshiftnote("<0 7 12>").osc().gain(0.15)
```

Source: `packages/core/controls.mjs`.

### fshiftphase

**Call:** `.fshiftphase(phase)`.

Phase of the frequency shifter, beside `fshift`. The browser synth does not read this control. It is registered with the other SuperDirt effects, next to `waveloss`.

```js
note("c3").s("sawtooth").fshift(40).fshiftphase("<0 .5 1>").osc().gain(0.15)
```

Source: `packages/core/controls.mjs`.

### ftrans

**Call:** `.ftrans(amt, edoSize)`. Same as `ftranspose`.

Frequency transpose. Assumes pattern either has `freq` set, or has values that can be interpreted as frequencies
amt has optional `edoSize` param, defaults to 12.
If haps have edoSize param set, such as from the output of `xen("31edo")`,
`ftrans` will fallback to that instead of 12 as the default.

Transposes the frequency by `amt` edoSteps

```js
i("0 1 2").xen("12edo").ftrans("7")
// n("0 1 2").scale("A:chromatic").trans("7")
```

```js
i("0 8 18").xen("31edo").ftrans("<8 -8>")
```

```js
// to transpose by steps of an edo, use "step:edo" :
i("0 7 8 18").xen("31edo").ftrans("<0 1:31 1:12>")
```

```js
// it can also work with frequency values directly
freq("200 300 400").ftrans("<0 7:31 7>")
```

Source: `packages/xen/xen.mjs`.

### fTrans

**Call:** `.fTrans(amt, edoSize)`. Same as `ftranspose`.

Frequency transpose. Assumes pattern either has `freq` set, or has values that can be interpreted as frequencies
amt has optional `edoSize` param, defaults to 12.
If haps have edoSize param set, such as from the output of `xen("31edo")`,
`ftrans` will fallback to that instead of 12 as the default.

Transposes the frequency by `amt` edoSteps

```js
i("0 1 2").xen("12edo").ftrans("7")
// n("0 1 2").scale("A:chromatic").trans("7")
```

```js
i("0 8 18").xen("31edo").ftrans("<8 -8>")
```

```js
// to transpose by steps of an edo, use "step:edo" :
i("0 7 8 18").xen("31edo").ftrans("<0 1:31 1:12>")
```

```js
// it can also work with frequency values directly
freq("200 300 400").ftrans("<0 7:31 7>")
```

Source: `packages/xen/xen.mjs`.

### ftranspose

**Call:** `.ftranspose(amt, edoSize)`. Aliases: `ftrans`, `fTrans`, `fTranspose`. Same as `ftranspose`.

Frequency transpose. Assumes pattern either has `freq` set, or has values that can be interpreted as frequencies
amt has optional `edoSize` param, defaults to 12.
If haps have edoSize param set, such as from the output of `xen("31edo")`,
`ftrans` will fallback to that instead of 12 as the default.

Transposes the frequency by `amt` edoSteps

```js
i("0 1 2").xen("12edo").ftrans("7")
// n("0 1 2").scale("A:chromatic").trans("7")
```

```js
i("0 8 18").xen("31edo").ftrans("<8 -8>")
```

```js
// to transpose by steps of an edo, use "step:edo" :
i("0 7 8 18").xen("31edo").ftrans("<0 1:31 1:12>")
```

```js
// it can also work with frequency values directly
freq("200 300 400").ftrans("<0 7:31 7>")
```

Source: `packages/xen/xen.mjs`.

### fTranspose

**Call:** `.fTranspose(amt, edoSize)`. Same as `ftranspose`.

Frequency transpose. Assumes pattern either has `freq` set, or has values that can be interpreted as frequencies
amt has optional `edoSize` param, defaults to 12.
If haps have edoSize param set, such as from the output of `xen("31edo")`,
`ftrans` will fallback to that instead of 12 as the default.

Transposes the frequency by `amt` edoSteps

```js
i("0 1 2").xen("12edo").ftrans("7")
// n("0 1 2").scale("A:chromatic").trans("7")
```

```js
i("0 8 18").xen("31edo").ftrans("<8 -8>")
```

```js
// to transpose by steps of an edo, use "step:edo" :
i("0 7 8 18").xen("31edo").ftrans("<0 1:31 1:12>")
```

```js
// it can also work with frequency values directly
freq("200 300 400").ftrans("<0 7:31 7>")
```

Source: `packages/xen/xen.mjs`.

### ftype

**Call:** `.ftype(type)`.

Sets the filter type. The ladder filter is more aggressive. More types might be added in the future.

```js
note("{f g g c d a a#}%8").s("sawtooth").lpenv(4).lpf(500).ftype("<0 1 2>").lpq(1)
```

```js
note("c f g g a c d4").fast(2)
.sound('sawtooth')
.lpf(200).fanchor(0)
.lpenv(3).lpq(1)
.ftype("<ladder 12db 24db>")
```

Source: `packages/core/controls.mjs`.

### FX

**Call:** `.FX(…)`.

Establishes an FX chain. Can be called by chaining .FX(fx1).FX(fx2)..
calls and/or in a single .FX(fx1, fx2, ..) call. The fx1, .. are _patterns_ which
establish the controls of the given effect. See examples.

```js
$: s("[sbd <hh [bd | lt | oh]>]*4").dec(.4)
  .FX(
    phaser(0.5).gain(2),
    bpf(800),
    distort(1.3),
    room(0.2),
    delay(0.5).gain(1.25),
    distort(0.3),
  ).fxr(1.7) // sets release time of effects (like delay)
```

```js
$: s("saw").fm(0.5)
  .delay(0.3) // outer effects are applied *last*
  .FX(coarse(4)) // first coarse
  .FX(lpf(500).lpe(4).lpa(1).lpd(2)) // then lpf
  .FX(distort(1)) // then distort
```

Source: `packages/core/pattern.mjs`.

### FXrelease

**Call:** `.FXrelease(seconds)`.

How long effects keep running after the note, in seconds. The played release is the longer of this value and `release`. Alias spellings `FXrel`, `FXr`, and `fxr` are the same control.

```js
note("c3 ~").s("sawtooth").release(0.05).room(0.4).FXrelease("<0.05 1>").gain(0.15)
```

Source: `packages/core/controls.mjs`.
