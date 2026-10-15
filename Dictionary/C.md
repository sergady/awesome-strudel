### C

- `ccn`
- `ccv`
- `ceil`
- `ch` — alias of `channels`
- `channel`
- `channels`
- `chebyshev`
- `chop`
- `chord`
- `chorus`
- `chunk`
- `chunkBack`
- `chunkback`
- `chunkBackInto`
- `chunkbackinto`
- `chunkInto`
- `chunkinto`
- `clearScope`
- `clip`
- `coarse`
- `color`
- `colour`
- `comb`
- `compress`
- `compressor`
- `compressorAttack`
- `compressorKnee`
- `compressorRatio`
- `compressorRelease`
- `compressSpan`
- `compressspan`
- `control`
- `cpm`
- `cps`
- `crush`
- `csound`
- `csoundm`
- `ctf` — alias of `lpf`
- `ctlNum`
- `ctranspose`
- `cubic`
- `curve`
- `cut`
- `cutoff`
- `cycleStruct`
- `cyclestruct`

## Entries

### ccn

**Call:** `.ccn()`.

MIDI control number: Sends a MIDI control change message.

Source: `packages/core/controls.mjs`.

### ccv

**Call:** `.ccv()`.

MIDI control value: Sends a MIDI control change message.

Source: `packages/core/controls.mjs`.

### ceil

**Call:** `.ceil()`.

Assumes a numerical pattern. Returns a new pattern with all values set to
their mathematical ceiling. E.g. `3.2` replaced with `4`, and `-4.2`
replaced with `-4`.

```js
note("42 42.1 42.5 43".ceil())
```

Source: `packages/core/pattern.mjs`.

### channel

**Call:** `.channel(channel)`.

Choose the channel the pattern is sent to

Source: `packages/core/controls.mjs`.

### channels

**Call:** `.channels(channels)`. Alias: `ch`.

Allows you to set the output channels on the interface

```js
note("e a d b g").channels("3:4")
```

Source: `packages/core/controls.mjs`.

### chebyshev

**Call:** `.chebyshev(distortion, volume)`.

Distortion via Chebyshev polynomials

Source: `packages/core/pattern.mjs`.

### chop

**Call:** `.chop(…)`.

Cuts each sample into the given number of parts, allowing you to explore a technique known as 'granular synthesis'.
It turns a pattern of samples into a pattern of parts of samples.

```js
samples({ rhodes: 'https://cdn.freesound.org/previews/132/132051_316502-lq.mp3' })
s("rhodes")
 .chop(4)
 .rev() // reverse order of chops
 .loopAt(2) // fit sample into 2 cycles
```

Source: `packages/core/pattern.mjs`.

### chord

**Call:** `.chord(symbols)`.

The chord to voice

```js
chord("<Am C D F Am E Am E>").voicing()
```

Source: `packages/core/controls.mjs`.

### chorus

**Call:** `.chorus(chorus)`.

mix control for the chorus effect

```js
note("d d a# a").s("sawtooth").chorus(.5)
```

Source: `packages/core/controls.mjs`.

### chunk

**Call:** `.chunk(…)`. Aliases: `slowChunk`, `slowchunk`.

Divides a pattern into a given number of parts, then cycles through those parts in turn, applying the given function to each part in turn (one part per cycle).

```js
"0 1 2 3".chunk(4, x=>x.add(7))
.scale("A:minor").note()
```

Source: `packages/core/pattern.mjs`.

### chunkBack

**Call:** `.chunkBack(…)`. Alias: `chunkback`.

Like `chunk`, but cycles through the parts in reverse order. Known as chunk' in tidalcycles

```js
"0 1 2 3".chunkBack(4, x=>x.add(7))
.scale("A:minor").note()
```

Source: `packages/core/pattern.mjs`.

### chunkback

**Call:** `.chunkback()`. Same as `chunkBack`.

Like `chunk`, but cycles through the parts in reverse order. Known as chunk' in tidalcycles

```js
"0 1 2 3".chunkBack(4, x=>x.add(7))
.scale("A:minor").note()
```

Source: `packages/core/pattern.mjs`.

### chunkBackInto

**Call:** `.chunkBackInto()`. Alias: `chunkbackinto`.

Like `chunkInto`, but moves backwards through the chunks.

```js
sound("bd sd ht lt bd - cp lt").chunkInto(4, hurry(2))
  .bank("tr909")
```

Source: `packages/core/pattern.mjs`.

### chunkbackinto

**Call:** `.chunkbackinto()`. Same as `chunkBackInto`.

Like `chunkInto`, but moves backwards through the chunks.

```js
sound("bd sd ht lt bd - cp lt").chunkInto(4, hurry(2))
  .bank("tr909")
```

Source: `packages/core/pattern.mjs`.

### chunkInto

**Call:** `.chunkInto(…)`. Alias: `chunkinto`.

Like `chunk`, but the function is applied to a looped subcycle of the source pattern.

```js
sound("bd sd ht lt bd - cp lt").chunkInto(4, hurry(2))
  .bank("tr909")
```

Source: `packages/core/pattern.mjs`.

### chunkinto

**Call:** `.chunkinto()`. Same as `chunkInto`.

Like `chunk`, but the function is applied to a looped subcycle of the source pattern.

```js
sound("bd sd ht lt bd - cp lt").chunkInto(4, hurry(2))
  .bank("tr909")
```

Source: `packages/core/pattern.mjs`.

### clearScope

**Call:** `clearScope`.

Clears all user-defined variables and functions from the scope.
This removes variables created during block-based evaluation.

```js
// After defining variables in blocks:
// let myVar = 5
// function myFunc() { return 10; }
clearScope() // removes myVar and myFunc from scope
```

Source: `packages/core/evaluate.mjs`.

### clip

**Call:** `.clip(factor)`. Alias: `legato`.

Multiplies the duration with the given number. Also cuts samples off at the end if they exceed the duration.

```js
note("c a f e").s("piano").clip("<.5 1 2>")
```

Source: `packages/core/controls.mjs`.

### coarse

**Call:** `.coarse(factor)`.

Fake-resampling for lowering the sample rate. Caution: This effect seems to only work in chromium based browsers

```js
s("bd sd [~ bd] sd,hh*8").coarse("<1 4 8 16 32>")
```

Source: `packages/core/controls.mjs`.

### color

**Call:** `.color(color)`. Alias: `colour`.

Sets the color of the hap in visualizations like pianoroll or highlighting.

Source: `packages/core/controls.mjs`.

### colour

**Call:** `.colour(color)`. Same as `color`.

Sets the color of the hap in visualizations like pianoroll or highlighting.

Source: `packages/core/controls.mjs`.

### comb

**Call:** `.comb(mix)`.

Comb-filter mix. The browser synth does not read this control. It is registered with the other SuperDirt effects, next to `waveloss`.

```js
note("c3").s("sawtooth").comb("<0 .4 .8>").osc().gain(0.15)
```

Source: `packages/core/controls.mjs`.

### compress

**Call:** `.compress()`.

Compress each cycle into the given timespan, leaving a gap


cat(
  s("bd sd").compress(.25,.75),
  s("~ bd sd ~")
)

Source: `packages/core/pattern.mjs`.

### compressor

**Call:** `.compressor(…)`.

Dynamics Compressor. The params are `compressor("threshold:ratio:knee:attack:release")`
More info [here](https://developer.mozilla.org/en-US/docs/Web/API/DynamicsCompressorNode?retiredLocale=de#instance_properties)

```js
s("bd sd [~ bd] sd,hh*8")
.compressor("-20:20:10:.002:.02")
```

Source: `packages/core/controls.mjs`.

### compressorAttack

**Call:** `.compressorAttack(seconds)`.

How many seconds the compressor takes to start reducing gain after the signal passes the threshold. `compressor` sets that threshold. Attack, knee, ratio, and release are the Web Audio compressor parameters.

```js
note("c3*4").s("sawtooth").compressor(-24).compressorRatio(8).compressorAttack("<0.005 .2>").gain(0.15)
```

Source: `packages/core/controls.mjs`.

### compressorKnee

**Call:** `.compressorKnee(decibels)`.

Width, in decibels, of the knee where compression begins. A wider knee eases into the reduction instead of switching it on at the threshold.

```js
note("c3*4").s("sawtooth").compressor(-18).compressorKnee("<0 10 30>").gain(0.15)
```

Source: `packages/core/controls.mjs`.

### compressorRatio

**Call:** `.compressorRatio(ratio)`.

How strongly the compressor turns the signal down once it is past the threshold. Higher ratios squash the peaks more.

```js
note("c3*8").s("sawtooth").gain("<0.05 0.4>").compressor(-12).compressorRatio("<1 4 12>")
```

Source: `packages/core/controls.mjs`.

### compressorRelease

**Call:** `.compressorRelease(seconds)`.

How many seconds the compressor takes to let go after the signal falls back under the threshold.

```js
note("c3*2").s("sawtooth").compressor(-20).compressorRatio(6).compressorRelease("<0.05 .4>").gain(0.15)
```

Source: `packages/core/controls.mjs`.

### compressSpan

**Call:** `.compressSpan(span)`.

Same work as `compress`: fit the pattern between two points in the cycle. The two points are `span.begin` and `span.end` on one value. `compressspan` is the same function.

```js
s("bd sd").compress(0.25, 0.75)
```

Source: `packages/core/pattern.mjs`.

### compressspan

**Call:** `.compressspan(span)`.

Same function as `compressSpan`. It reads `begin` and `end` from one value and fits the pattern into that slice of the cycle.

```js
s("bd sd").compressspan({begin: 0.25, end: 0.75})
```

Source: `packages/core/pattern.mjs`.

### control

**Call:** `.control()`.

MIDI control: Sends a MIDI control change message.

Source: `packages/core/controls.mjs`.

### cpm

**Call:** `.cpm(cyclesPerMinute)`.

Plays this pattern at the given number of cycles per minute. In the editor, that is relative to the clock already set by `setcpm` or `setcps`. The copy in `pattern.mjs` is marked deprecated and assumes one cycle per second.

```js
s("<bd sd>,hh*2").cpm(90)
```

Source: `packages/core/pattern.mjs`.

### cps

**Call:** `.cps(cyclesPerSecond)`.

Writes a cycles-per-second value onto the event. It does not change the editor clock. The clock functions are `setcps` and `setcpm`. This control is registered with the other playback-metadata controls (`hours`, `minutes`, `seconds`, `songPtr`).

```js
note("c4*4").s("triangle").cps(0.5).gain(0.2)
```

Source: `packages/core/controls.mjs`.

### crush

**Call:** `.crush(depth)`.

Bit crusher effect.

```js
s("<bd sd>,hh*3").fast(2).crush("<16 8 7 6 5 4 3 2>")
```

Source: `packages/core/controls.mjs`.

### csound

**Call:** `.csound(instrument)`.

Sends each event to a Csound instrument. The instrument name defaults to `triangle`. `@strudel/csound` is not loaded by the default editor prebake.

```js
note("c4 e4 g4").csound("triangle").gain(0.2)
```

Source: `packages/csound/index.mjs`.

### csoundm

**Call:** `.csoundm()`.

Sends notes to Csound for rendering with MIDI semantics. The hap value is
translated to these Csound pfields:

 p1 -- Csound instrument either as a number (1-based, can be a fraction),
       or as a string name.
 p2 -- time in beats (usually seconds) from start of performance.
 p3 -- duration in beats (usually seconds).
 p4 -- MIDI key number (as a real number, not an integer but in [0, 127].
 p5 -- MIDI velocity (as a real number, not an integer but in [0, 127].
 p6 -- Strudel controls, as a string.

Source: `packages/csound/index.mjs`.

### ctlNum

**Call:** `.ctlNum(number)`.

A MIDI controller-number control. The MIDI output in this checkout sends `ccn` together with `ccv`, and does not read `ctlNum`.

```js
note("c4").ctlNum(74).ccv(0.5).midi()
```

Source: `packages/core/controls.mjs`.

### ctranspose

**Call:** `.ctranspose(amount)`.

Registered control. The source says it was not found in the Tidal documentation, and this checkout does not apply it.

```js
note("c4 e4 g4").s("triangle").ctranspose(1).gain(0.2)
```

Source: `packages/core/controls.mjs`.

### cubic

**Call:** `.cubic(distortion, volume)`.

Cubic polynomial distortion

Source: `packages/core/pattern.mjs`.

### curve

**Call:** `.curve(amount)`.

Waveshape curve of a ZZFX sound (`zzfx`, `z_sine`, `z_sawtooth`, and the other `z_` names). The synth raises the waveform to this power. The ZZFX comment treats 0 as square and 2 as pointy. A square ZZFX wave forces the curve to 0.

```js
s("z_sawtooth").note("c3").curve("<0 1 2>").gain(0.2)
```

Source: `packages/core/controls.mjs`.

### cut

**Call:** `.cut(group)`.

In the style of classic drum-machines, `cut` will stop a playing sample as soon as another samples with in same cutgroup is to be played. An example would be an open hi-hat followed by a closed one, essentially muting the open.

```js
s("[oh hh]*4").cut(1)
```

Source: `packages/core/controls.mjs`.

### cutoff

**Call:** `.cutoff(frequency)`. Same as `lpf`.

Applies the cutoff frequency of the **l**ow-**p**ass **f**ilter.

When using mininotation, you can also optionally add the 'lpq' parameter, separated by ':'.

```js
s("bd sd [~ bd] sd,hh*6").lpf("<4000 2000 1000 500 200 100>")
```

```js
s("bd*16").lpf("1000:0 1000:10 1000:20 1000:30")
```

Source: `packages/core/controls.mjs`.

### cycleStruct

**Call:** `.cycleStruct(structure)`. Same as `isobite`.

Similar to `struct`, but every hap in the structure pattern plays the next
cycle of the main pattern.
With a different number of cycles in the main pattern and haps in the
structure pattern, this creates an isorhythm.

Note: This function works on the assumption that the structure pattern
repeats every cycle. If the structure pattern only repeats after multiple
cycles, it may skip or repeat certain parts of the melody.

```js
"<0 1 2 3 4 5>".isobite("[x - x*2]*2").n().scale("c:major")
// the same as "0 - [1 2] 3 - [4 5]".n().scale("c:major")
```

```js
"<0 1 2 3 4>".isobite("x - x").n().scale("c:major")
// the same as "<[0 - 1] [2 - 3] [4 - 0] [1 - 2] [3 - 4]>".n().scale("c:major")
```

```js
// Here the structure pattern repeats after 2 cycles,
// so certain haps from the melody are skipped.
"<0 1 2 3>".isobite("x x*2".slow(2)).n().scale("c:major")
// the same as "<[0] [2 3] [2] [2 3]>".n().scale("c:major")
```

```js
// This can be avoided by making the struct pattern 1 cycle,
// and slowing the whole pattern down as follows:
"<0 1 2 3>".isobite("x x*2").slow(2).n().scale("c:major")
// the same as "<[0] [1 2] [3] [0 1] [2] [3 0] [1] [2 3]>".n().scale("c:major")
```

Source: `packages/core/pattern.mjs`.

### cyclestruct

**Call:** `.cyclestruct(structure)`. Same as `isobite`.

Similar to `struct`, but every hap in the structure pattern plays the next
cycle of the main pattern.
With a different number of cycles in the main pattern and haps in the
structure pattern, this creates an isorhythm.

Note: This function works on the assumption that the structure pattern
repeats every cycle. If the structure pattern only repeats after multiple
cycles, it may skip or repeat certain parts of the melody.

```js
"<0 1 2 3 4 5>".isobite("[x - x*2]*2").n().scale("c:major")
// the same as "0 - [1 2] 3 - [4 5]".n().scale("c:major")
```

```js
"<0 1 2 3 4>".isobite("x - x").n().scale("c:major")
// the same as "<[0 - 1] [2 - 3] [4 - 0] [1 - 2] [3 - 4]>".n().scale("c:major")
```

```js
// Here the structure pattern repeats after 2 cycles,
// so certain haps from the melody are skipped.
"<0 1 2 3>".isobite("x x*2".slow(2)).n().scale("c:major")
// the same as "<[0] [2 3] [2] [2 3]>".n().scale("c:major")
```

```js
// This can be avoided by making the struct pattern 1 cycle,
// and slowing the whole pattern down as follows:
"<0 1 2 3>".isobite("x x*2").slow(2).n().scale("c:major")
// the same as "<[0] [1 2] [3] [0 1] [2] [3 0] [1] [2 3]>".n().scale("c:major")
```

Source: `packages/core/pattern.mjs`.
