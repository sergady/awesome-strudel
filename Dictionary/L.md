### L

- `label`
- `lastOf`
- `late`
- `layer`
- `lbrick`
- `legato` — alias of `clip`
- `leslie`
- `lfo`
- `linger`
- `lock`
- `log`
- `log2`
- `logValues`
- `loop`
- `loopAt`
- `loopat`
- `loopAtCps`
- `loopatcps`
- `loopb` — alias of `loopBegin`
- `loopBegin`
- `loope` — alias of `loopEnd`
- `loopEnd`
- `lp` — alias of `lpf`
- `lpa` — alias of `lpattack`
- `lpattack`
- `lpd` — alias of `lpdecay`
- `lpdc`
- `lpdecay`
- `lpdepth`
- `lpdepthfreq` — alias of `lpdepthfrequency`
- `lpdepthfrequency`
- `lpe` — alias of `lpenv`
- `lpenv`
- `lpf`
- `lpq`
- `lpr` — alias of `lprelease`
- `lprate`
- `lprelease`
- `lps` — alias of `lpsustain`
- `lpshape`
- `lpskew`
- `lpsustain`
- `lpsync`
- `lrate`
- `lsize`
- `lt`
- `lte`

## Entries

### label

**Call:** `.label(label)`.

Sets the displayed text for an event on the pianoroll

Source: `packages/core/controls.mjs`.

### lastOf

**Call:** `.lastOf(n, func)`.

Applies the given function every n cycles, starting from the last cycle.

```js
note("c3 d3 e3 g3").lastOf(4, x=>x.rev())
```

Source: `packages/core/pattern.mjs`.

### late

**Call:** `.late(cycles)`.

Nudge a pattern to start later in time. Equivalent of Tidal's ~> operator

```js
"bd ~".stack("hh ~".late(.1)).s()
```

Source: `packages/core/pattern.mjs`.

### layer

**Call:** `.layer(…)`.

Layers the result of the given function(s). Like `superimpose`, but without the original pattern:

```js
"<0 2 4 6 ~ 4 ~ 2 0!3 ~!5>*8"
  .layer(x=>x.add("0,2"))
  .scale('C minor').note()
```

Source: `packages/core/pattern.mjs`.

### lbrick

**Call:** `.lbrick(frequency)`.

Low brickwall cutoff. The browser synth does not read this control. It is registered with the other SuperDirt effects, next to `waveloss`.

```js
note("c3").s("sawtooth").lbrick("<100 800>").osc().gain(0.15)
```

Source: `packages/core/controls.mjs`.

### leslie

**Call:** `.leslie(wet)`.

Emulation of a Leslie speaker: speakers rotating in a wooden amplified cabinet.

```js
n("0,4,7").s("supersquare").leslie("<0 .4 .6 1>").osc()
```

Source: `packages/core/controls.mjs`.

### lfo

**Call:** `.lfo(config, id)`.

Configures an LFO. Can be called in sequence like pat.lfo(...).lfo(...) to set up multiple LFOs.
There are two ways to declare which control will be modulated:
1. Explicitly put `control` in the config (e.g. `lfo({ c: "lpf" })`)
2. If the control parameter is absent, the control _immediately before_ the `lfo` call will be used
  (e.g. `s("saw").lpf(500).lfo()` to modulate `lpf`)

Modulators can be referred to by `id` so that they can be updated later e.g. inside
a `sometimes`. See example below.

```js
s("saw").note("F1").lpf(500).lfo()
```

```js
s("saw").lfo().lpf(500).lfo({ s: 0.3 })
```

```js
s("saw").lpf(500).diode(0.3)
  .lfo({ c: "lpf" })
```

```js
s("pulse").lpf(500).lfo()
  .lfo({ c: "s" })
  .diode(0.3)
  .sometimes(x => x.lfo({ s: "8" }, 1)) // lfo #1 (0-indexed)
```

```js
s("pulse").lpf(500).lfo({ depth: 4 }, 'lpf_mod')
  .lfo({ c: "s" })
  .diode(0.3)
  .sometimes(x => x.lfo({ s: "8" }, 'lpf_mod'))
```

Source: `packages/core/controls.mjs`.

### linger

**Call:** `.linger()`.

Selects the given fraction of the pattern and repeats that part to fill the remainder of the cycle.



s("lt ht mt cp, [hh oh]*2").linger("<1 .5 .25 .125>")

Source: `packages/core/pattern.mjs`.

### lock

**Call:** `.lock(enable)`.

Specifies whether delaytime is calculated relative to cps.

```js
s("sd").delay().lock(1).osc()
```

Source: `packages/core/controls.mjs`.

### log

**Call:** `.log()`.

Writes the content of the current event to the console (visible in the side menu).

```js
s("bd sd").log()
```

Source: `packages/core/pattern.mjs`.

### log2

**Call:** `.log2()`.

Base-2 logarithm of each number. 1, 2, 4, 8 become 0, 1, 2, 3.

```js
n("1 2 4 8".log2()).scale("C4:major").s("triangle").gain(0.2)
```

Source: `packages/core/pattern.mjs`.

### logValues

**Call:** `.logValues()`.

A simplified version of `log` which writes all "values" (various configurable parameters)
within the event to the console (visible in the side menu).

```js
s("bd sd").gain("0.25 0.5 1").n("2 1 0").logValues()
```

Source: `packages/core/pattern.mjs`.

### loop

**Call:** `.loop(on)`.

Loops the sample.
Note that the tempo of the loop is not synced with the cycle tempo.
To change the loop region, use loopBegin / loopEnd.

```js
s("casio").loop(1)
```

Source: `packages/core/controls.mjs`.

### loopAt

**Call:** `.loopAt(…)`.

Makes the sample fit the given number of cycles by changing the speed.

```js
samples({ rhodes: 'https://cdn.freesound.org/previews/132/132051_316502-lq.mp3' })
s("rhodes").loopAt(2)
```

Source: `packages/core/pattern.mjs`.

### loopat

**Call:** `.loopat(cycles)`.

Same function as `loopAt`. Changes the sample speed so the sample lasts the given number of cycles.

```js
s("piano").loopat(4)
```

Source: `packages/core/pattern.mjs`.

### loopAtCps

**Call:** `.loopAtCps(…)`.

Makes the sample fit the given number of cycles and cps value, by
changing the speed. deprecated: use loopAt or fit instead, together with setCps / setCpm.

```js
samples({ rhodes: 'https://cdn.freesound.org/previews/132/132051_316502-lq.mp3' })
s("rhodes").loopAtCps(4,1.5).cps(1.5)
```

Source: `packages/core/pattern.mjs`.

### loopatcps

**Call:** `.loopatcps(cycles, cps)`.

Same function as `loopAtCps`. Fits the sample to `cycles` at the given cycles per second. The source marks it deprecated in favor of `loopAt` or `fit` together with `setcps`.

```js
s("piano").loopatcps(4, 0.5)
```

Source: `packages/core/pattern.mjs`.

### loopBegin

**Call:** `.loopBegin(time)`. Alias: `loopb`.

Begin to loop at a specific point in the sample (inbetween `begin` and `end`).
Note that the loop point must be inbetween `begin` and `end`, and before `loopEnd`!
Note: Samples starting with wt_ will automatically loop! (wt = wavetable)

```js
s("space").loop(1)
.loopBegin("<0 .125 .25>")._scope()
```

Source: `packages/core/controls.mjs`.

### loopEnd

**Call:** `.loopEnd(time)`. Alias: `loope`.

End the looping section at a specific point in the sample (inbetween `begin` and `end`).
Note that the loop point must be inbetween `begin` and `end`, and after `loopBegin`!

```js
s("space").loop(1)
.loopEnd("<1 .75 .5 .25>")._scope()
```

Source: `packages/core/controls.mjs`.

### lpattack

**Call:** `.lpattack(attack)`. Alias: `lpa`.

Sets the attack duration for the lowpass filter envelope.

```js
note("c2 e2 f2 g2")
.sound('sawtooth')
.lpf(300)
.lpa("<.5 .25 .1 .01>/4")
.lpenv(4)
```

Source: `packages/core/controls.mjs`.

### lpdc

**Call:** `.lpdc(dcoffset)`.

DC offset of the LFO for the lowpass filter

Source: `packages/core/controls.mjs`.

### lpdecay

**Call:** `.lpdecay(decay)`. Alias: `lpd`.

Sets the decay duration for the lowpass filter envelope.

```js
note("c2 e2 f2 g2")
.sound('sawtooth')
.lpf(300)
.lpd("<.5 .25 .1 0>/4")
.lpenv(4)
```

Source: `packages/core/controls.mjs`.

### lpdepth

**Call:** `.lpdepth(depth)`.

Depth of the LFO for the lowpass filter

```js
note("<c c c# c c c4>*16").s("sawtooth").lpf(600).lpdepth("<1 .5 1.8 0>")
```

Source: `packages/core/controls.mjs`.

### lpdepthfrequency

**Call:** `.lpdepthfrequency(depth)`. Alias: `lpdepthfreq`.

Depth of the LFO for the lowpass filter, in HZ

```js
note("<c c c# c c c4>*16").s("sawtooth").lpf(600).lpdepthfrequency("<200 500 100 0>")
```

Source: `packages/core/controls.mjs`.

### lpenv

**Call:** `.lpenv(modulation)`. Alias: `lpe`.

Sets the lowpass filter envelope modulation depth.

```js
note("c2 e2 f2 g2")
.sound('sawtooth')
.lpf(300)
.lpa(.5)
.lpenv("<4 2 1 0 -1 -2 -4>/4")
```

Source: `packages/core/controls.mjs`.

### lpf

**Call:** `.lpf(frequency)`. Aliases: `cutoff`, `ctf`, `lp`.

Applies the cutoff frequency of the **l**ow-**p**ass **f**ilter.

When using mininotation, you can also optionally add the 'lpq' parameter, separated by ':'.

```js
s("bd sd [~ bd] sd,hh*6").lpf("<4000 2000 1000 500 200 100>")
```

```js
s("bd*16").lpf("1000:0 1000:10 1000:20 1000:30")
```

Source: `packages/core/controls.mjs`.

### lpq

**Call:** `.lpq(q)`. Alias: `resonance`.

Controls the **l**ow-**p**ass **q**-value.

```js
s("bd sd [~ bd] sd,hh*8").lpf(2000).lpq("<0 10 20 30>")
```

Source: `packages/core/controls.mjs`.

### lprate

**Call:** `.lprate(rate)`.

Rate of the LFO for the lowpass filter

```js
note("<c c c# c c c4>*16").s("sawtooth").lpf(600).lprate("<4 8 2 1>")
```

Source: `packages/core/controls.mjs`.

### lprelease

**Call:** `.lprelease(release)`. Alias: `lpr`.

Sets the release time for the lowpass filter envelope.

```js
note("c2 e2 f2 g2")
.sound('sawtooth')
.clip(.5)
.lpf(300)
.lpenv(4)
.lpr("<.5 .25 .1 0>/4")
.release(.5)
```

Source: `packages/core/controls.mjs`.

### lpshape

**Call:** `.lpshape(shape)`.

Shape of the LFO for the lowpass filter

Source: `packages/core/controls.mjs`.

### lpskew

**Call:** `.lpskew(skew)`.

Skew of the LFO for the lowpass filter

Source: `packages/core/controls.mjs`.

### lpsustain

**Call:** `.lpsustain(sustain)`. Alias: `lps`.

Sets the sustain amplitude for the lowpass filter envelope.

```js
note("c2 e2 f2 g2")
.sound('sawtooth')
.lpf(300)
.lpd(.5)
.lps("<0 .25 .5 1>/4")
.lpenv(4)
```

Source: `packages/core/controls.mjs`.

### lpsync

**Call:** `.lpsync(rate)`.

Cycle-synced rate of the LFO for the lowpass filter

```js
note("<c c c# c c c4>*16").s("sawtooth").lpf(600).lpsync("<4 8 2 1>")
```

Source: `packages/core/controls.mjs`.

### lrate

**Call:** `.lrate(rate)`.

Rate of modulation / rotation for leslie effect

```js
n("0,4,7").s("supersquare").leslie(1).lrate("<1 2 4 8>").osc()
```

Source: `packages/core/controls.mjs`.

### lsize

**Call:** `.lsize(meters)`.

Physical size of the cabinet in meters. Be careful, it might be slightly larger than your computer. Affects the Doppler amount (pitch warble)

```js
n("0,4,7").s("supersquare").leslie(1).lrate(2).lsize("<.1 .5 1>").osc()
```

Source: `packages/core/controls.mjs`.

### lt

**Call:** `lt(a, b)`.

performs a < b

Source: `packages/core/pattern.mjs`.

### lte

**Call:** `lte(a, b)`.

performs a <= b

Source: `packages/core/pattern.mjs`.
