### P

- `pace`
- `palindrome`
- `pan`
- `panchor`
- `panorient`
- `panspan`
- `pansplay`
- `panwidth`
- `parray`
- `partials`
- `patt` — alias of `pattack`
- `pattack`
- `pcurve`
- `pdec` — alias of `pdecay`
- `pdecay`
- `penv`
- `perlin`
- `ph` — alias of `phaser`
- `phasdp` — alias of `phaserdepth`
- `phaser`
- `phasercenter`
- `phaserdepth`
- `phaserrate`
- `phasersweep`
- `phases`
- `phc` — alias of `phasercenter`
- `phd` — alias of `phaserdepth`
- `phs` — alias of `phasersweep`
- `pianoroll`
- `pick`
- `pickF`
- `pickmod`
- `pickmodF`
- `pickmodOut`
- `pickmodReset`
- `pickmodRestart`
- `pickmodSqueeze`
- `pickOut`
- `pickReset`
- `pickRestart`
- `pickSqueeze`
- `pitchJump`
- `pitchJumpTime`
- `pitchwheel`
- `ply`
- `plyForEach`
- `plyforeach`
- `plyWith`
- `plywith`
- `polyTouch`
- `postgain`
- `pow`
- `prel` — alias of `prelease`
- `prelease`
- `press`
- `pressBy`
- `progNum`
- `psustain`
- `punchcard` — alias of `pianoroll`
- `pw`
- `pwr` — alias of `pwrate`
- `pwrate`
- `pws` — alias of `pwsweep`
- `pwsweep`

## Entries

### pace

**Call:** `.pace()`.

*Experimental*

Speeds a pattern up or down, to fit to the given number of steps per cycle.


sound("bd sd cp").pace(4)
// The same as sound("{bd sd cp}%4") or sound("<bd sd cp>*4")

Source: `packages/core/pattern.mjs`.

### palindrome

**Call:** `.palindrome()`.

Applies `rev` to a pattern every other cycle, so that the pattern alternates between forwards and backwards.


note("c d e g").palindrome()

Source: `packages/core/pattern.mjs`.

### pan

**Call:** `.pan(pan)`.

Sets position in stereo.

```js
s("[bd hh]*2").pan("<.5 1 .5 0>")
```

```js
s("bd rim sd rim bd ~ cp rim").pan(sine.slow(2))
```

Source: `packages/core/controls.mjs`.

### panchor

**Call:** `.panchor(anchor)`.

Sets the range anchor of the envelope:
- anchor 0: range = [note, note + penv]
- anchor 1: range = [note - penv, note]
If you don't set an anchor, the value will default to the psustain value.

```js
note("c c4").penv(12).panchor("<0 .5 1 .5>")
```

Source: `packages/core/controls.mjs`.

### panorient

**Call:** `.panorient(direction)`.

Registered beside `pan`, `panspan`, and `pansplay`. The browser synth reads `pan` only, not this control.

```js
s("bd*4").pan("<0 1>").panorient(0.5)
```

Source: `packages/core/controls.mjs`.

### panspan

**Call:** `.panspan(span)`.

Controls how much multichannel output is fanned out

```js
s("[bd hh]*2").pan("<.5 1 .5 0>").panspan("<0 .5 1>").osc()
```

Source: `packages/core/controls.mjs`.

### pansplay

**Call:** `.pansplay(spread)`.

Controls how much multichannel output is spread

```js
s("[bd hh]*2").pan("<.5 1 .5 0>").pansplay("<0 .5 1>").osc()
```

Source: `packages/core/controls.mjs`.

### panwidth

**Call:** `.panwidth(width)`.

Registered beside `pansplay`. The browser synth reads `pan` only, not this control.

```js
s("bd*4").pan("<0 1>").panwidth("<0.2 1>")
```

Source: `packages/core/controls.mjs`.

### parray

**Call:** `parray`.

Turns a list of patterns into a single pattern which outputs list-values

Source: `packages/core/pattern.mjs`.

### partials

**Call:** `.partials(magnitudes)`.

Scale the magnitude of the harmonics of one of the core synths ('sine', 'tri', 'saw', ..)

Can also be used to create a new synth via `s('user').partials(...)`

```js
s("user").seg(16).n(irand(8)).scale("A:major")
  .partials([1, 0, 1, 0, 0, 1])
```

```js
s("saw").seg(8).n(irand(12)).scale("G#:minor")
  .partials(binaryL(irand(256).add("1")))
```

Source: `packages/core/pattern.mjs`.

### pattack

**Call:** `.pattack(time)`. Alias: `patt`.

Attack time of pitch envelope.

```js
note("c eb g bb").pattack("0 .1 .25 .5").slow(2)
```

Source: `packages/core/controls.mjs`.

### pcurve

**Call:** `.pcurve(type)`.

Curve of envelope. Defaults to linear. exponential is good for kicks

```js
note("g1*4")
.s("sine").pdec(.5)
.penv(32)
.pcurve("<0 1>")
```

Source: `packages/core/controls.mjs`.

### pdecay

**Call:** `.pdecay(time)`. Alias: `pdec`.

Decay time of pitch envelope.

```js
note("<c eb g bb>").pdecay("<0 .1 .25 .5>")
```

Source: `packages/core/controls.mjs`.

### penv

**Call:** `.penv(semitones)`.

Amount of pitch envelope. Negative values will flip the envelope.
If you don't set other pitch envelope controls, `pattack:.2` will be the default.

```js
note("c")
.penv("<12 7 1 .5 0 -1 -7 -12>")
```

Source: `packages/core/controls.mjs`.

### perlin

**Call:** `perlin`.

Generates a continuous pattern of [perlin noise](https://en.wikipedia.org/wiki/Perlin_noise), in the range 0..1.

```js
// randomly change the cutoff
s("bd*4,hh*8").cutoff(perlin.range(500,8000))
```

Source: `packages/core/signal.mjs`.

### phaser

**Call:** `.phaser(speed)`. Alias: `ph`.

Phaser audio effect that approximates popular guitar pedals.

```js
n(run(8)).scale("D:pentatonic").s("sawtooth").release(0.5)
.phaser("<1 2 4 8>")
```

Source: `packages/core/controls.mjs`.

### phasercenter

**Call:** `.phasercenter(centerfrequency)`. Alias: `phc`.

The center frequency of the phaser in HZ. Defaults to 1000

```js
n(run(8)).scale("D:pentatonic").s("sawtooth").release(0.5)
.phaser(2).phasercenter("<800 2000 4000>")
```

Source: `packages/core/controls.mjs`.

### phaserdepth

**Call:** `.phaserdepth(depth)`. Aliases: `phd`, `phasdp`.

The amount the signal is affected by the phaser effect. Defaults to 0.75

```js
n(run(8)).scale("D:pentatonic").s("sawtooth").release(0.5)
.phaser(2).phaserdepth("<0 .5 .75 1>")
```

Source: `packages/core/controls.mjs`.

### phaserrate

**Call:** `.phaserrate(hertz)`.

Speed of the phaser's tremolo, in hertz. The phaser is built only when `phaserdepth` is greater than 0.

```js
note("c3").s("sawtooth").phaserdepth(0.8).phaserrate("<0.2 2 6>").gain(0.12)
```

Source: `packages/core/controls.mjs`.

### phasersweep

**Call:** `.phasersweep(phasersweep)`. Alias: `phs`.

The frequency sweep range of the lfo for the phaser effect. Defaults to 2000

```js
n(run(8)).scale("D:pentatonic").s("sawtooth").release(0.5)
.phaser(2).phasersweep("<800 2000 4000>")
```

Source: `packages/core/controls.mjs`.

### phases

**Call:** `.phases(phases)`.

Rotates the harmonics of one of the core synths ('sine', 'tri', 'saw', 'user', ..) by a list of phases

```js
// Phase cancellation
s("saw").seg(8).n(irand(12)).scale("G#1:minor")
  .partials(partials([1, 1, 1]))
  .superimpose(x => x.phases([0.5, 0.5, 0.5]))
```

Source: `packages/core/pattern.mjs`.

### pianoroll

**Call:** `.pianoroll(options, cycles, playhead, vertical, labels, flipTime, flipValues, overscan, hideNegative, smear, fold, active, inactive, background, playheadColor, fill, fillActive, stroke, strokeActive, hideInactive, colorizeInactive, fontFamily, minMidi, maxMidi, autorange)`. Alias: `punchcard`.

Visualises a pattern as a scrolling 'pianoroll', displayed in the background of the editor. To show a pianoroll for all running patterns, use `all(pianoroll)`. To have a pianoroll appear below
a pattern instead, prefix with `_`, e.g.: `sound("bd sd")._pianoroll()`.

```js
note("c2 a2 eb2")
.euclid(5,8)
.s('sawtooth')
.lpenv(4).lpf(300)
.pianoroll({ labels: 1 })
```

Source: `packages/draw/pianoroll.mjs`.

### pick

**Call:** `.pick(list)`.

Uses each value as an index into a list or object of patterns, and plays the chosen pattern. The index keeps the time structure of the index pattern.

```js
sound("<0 1 [2,0]>".pick(["bd sd", "cp cp", "hh hh"]))
```

Source: `packages/core/pick.mjs`.

### pickF

**Call:** `.pickF()`.

pickF lets you use a pattern of numbers to pick which function to apply to another pattern.






s("bd [rim hh]").pickF("<0 1 2>", [rev,jux(rev),fast(2)])

note("<c2 d2>(3,8)").s("square")
.pickF("<0 2> 1", [jux(rev), fast(2), x=>x.lpf(800)])

note("<c2 d2>(3,8)").s("square")
.pickF("<jr l> f", { jr:jux(rev), f:fast(2), l:x=>x.lpf(800) })

Source: `packages/core/pick.mjs`.

### pickmod

**Call:** `.pickmod()`.

The same as `pick`, but if you pick a number greater than the size of the list,
it wraps around, rather than sticking at the maximum value.
For example, if you pick the fifth pattern of a list of three, you'll get the
second one.

Source: `packages/core/pick.mjs`.

### pickmodF

**Call:** `.pickmodF()`.

The same as `pickF`, but if you pick a number greater than the size of the functions list,
it wraps around, rather than sticking at the maximum value.

Source: `packages/core/pick.mjs`.

### pickmodOut

**Call:** `.pickmodOut()`.

The same as `pickOut`, but if you pick a number greater than the size of the list,
it wraps around, rather than sticking at the maximum value.

Source: `packages/core/pick.mjs`.

### pickmodReset

**Call:** `.pickmodReset()`.

The same as `pickReset`, but if you pick a number greater than the size of the list,
it wraps around, rather than sticking at the maximum value.

Source: `packages/core/pick.mjs`.

### pickmodRestart

**Call:** `.pickmodRestart()`.

The same as `pickRestart`, but if you pick a number greater than the size of the list,
it wraps around, rather than sticking at the maximum value.





"<a
        a: n("0 1 2 0"),
        b: n("2 3 4 ~"),
        c: n("[4 5] [4 3] 2 0"),
        d: n("0 -3 0 ~")
      }).scale("C:major").s("piano")

Source: `packages/core/pick.mjs`.

### pickmodSqueeze

**Call:** `.pickmodSqueeze(pat, xs)`. Same as `inhabitmod`.

The same as `inhabit`, but if you pick a number greater than the size of the list,
it wraps around, rather than sticking at the maximum value.
For example, if you pick the fifth pattern of a list of three, you'll get the
second one.

Source: `packages/core/pick.mjs`.

### pickOut

**Call:** `.pickOut()`.

Similar to `pick`, but it applies an outerJoin instead of an innerJoin.





note("<0*4 1 2*2 3*3>".pickOut(["g a", "e f", "f g f g" , "g c d"]))

Source: `packages/core/pick.mjs`.

### pickReset

**Call:** `.pickReset()`.

Similar to `pick`, but the choosen pattern is reset when its index is triggered.

Source: `packages/core/pick.mjs`.

### pickRestart

**Call:** `.pickRestart()`.

Similar to `pick`, but the choosen pattern is restarted when its index is triggered.

Source: `packages/core/pick.mjs`.

### pickSqueeze

**Call:** `.pickSqueeze(pat, xs)`. Same as `inhabit`.

Picks patterns (or plain values) either from a list (by index) or a lookup table (by name).
Similar to `pick`, but cycles are squeezed into the target ('inhabited') pattern.

```js
let a = s("bd(3,8)")
let b = s("cp sd")
"<a b [a,b]>".inhabit({ a, b })
```

```js
s("a@2 [a b] a"
.inhabit({a: "bd(3,8)", b: "sd sd"}))
.slow(4)
```

Source: `packages/core/pick.mjs`.

### pitchJump

**Call:** `.pitchJump(amount)`.

Size of a one-time pitch jump in a ZZFX sound. `pitchJumpTime` is when that jump happens.

```js
s("z_sine").note("c3").pitchJump("<0 200 600>").pitchJumpTime(0.1).gain(0.2)
```

Source: `packages/core/controls.mjs`.

### pitchJumpTime

**Call:** `.pitchJumpTime(time)`.

When the ZZFX `pitchJump` happens, as the synth's time parameter.

```js
s("z_sawtooth").note("c3").pitchJump(400).pitchJumpTime("<0.02 .1 .2>").gain(0.2)
```

Source: `packages/core/controls.mjs`.

### pitchwheel

**Call:** `.pitchwheel(hapcircles, circle, edo, root, thickness, hapRadius, mode, margin)`.

Renders a pitch circle to visualize frequencies within one octave

```js
n("0 .. 12").scale("C:chromatic")
.s("sawtooth")
.lpf(500)
._pitchwheel()
```

Source: `packages/draw/pitchwheel.mjs`.

### ply

**Call:** `.ply()`.

The ply function repeats each event the given number of times.


s("bd ~ sd cp").ply("<1 2 3>")

Source: `packages/core/pattern.mjs`.

### plyForEach

**Call:** `.plyForEach(factor, func)`. Alias: `plyforeach`.

The plyForEach function repeats each event the given number of times, applying the given function to each event.
This version of ply uses the iteration index as an argument to the function, similar to echoWith.

```js
"<0 [2 4]>"
.plyForEach(4, (p,n) => p.add(n*2))
.scale("C:minor").note()
```

Source: `packages/core/pattern.mjs`.

### plyforeach

**Call:** `.plyforeach(factor, func)`. Same as `plyForEach`.

The plyForEach function repeats each event the given number of times, applying the given function to each event.
This version of ply uses the iteration index as an argument to the function, similar to echoWith.

```js
"<0 [2 4]>"
.plyForEach(4, (p,n) => p.add(n*2))
.scale("C:minor").note()
```

Source: `packages/core/pattern.mjs`.

### plyWith

**Call:** `.plyWith(factor, func)`. Alias: `plywith`.

The plyWith function repeats each event the given number of times, applying the given function to each event.\n

```js
"<0 [2 4]>"
.plyWith(4, (p) => p.add(2))
.scale("C:minor").note()
```

Source: `packages/core/pattern.mjs`.

### plywith

**Call:** `.plywith(factor, func)`. Same as `plyWith`.

The plyWith function repeats each event the given number of times, applying the given function to each event.\n

```js
"<0 [2 4]>"
.plyWith(4, (p) => p.add(2))
.scale("C:minor").note()
```

Source: `packages/core/pattern.mjs`.

### polyTouch

**Call:** `.polyTouch(pressure)`.

Polyphonic aftertouch for a MIDI note. The MIDI output reads the value off the event and does not send a polyphonic-aftertouch message.

```js
note("c4 e4 g4").polyTouch("<0 .5 1>").midi()
```

Source: `packages/core/controls.mjs`.

### postgain

**Call:** `.postgain(…)`.

Gain applied after all effects have been processed.

```js
s("bd sd [~ bd] sd,hh*8")
.compressor("-20:20:10:.002:.02").postgain(1.5)
```

Source: `packages/core/controls.mjs`.

### pow

**Call:** `pow`.

Raises each number to the power of the given factor

Source: `packages/core/pattern.mjs`.

### prelease

**Call:** `.prelease(time)`. Alias: `prel`.

Release time of pitch envelope

```js
note("<c eb g bb> ~")
.release(.5) // to hear the pitch release
.prelease("<0 .1 .25 .5>")
```

Source: `packages/core/controls.mjs`.

### press

**Call:** `.press()`.

Syncopates a rhythm, by shifting each event halfway into its timespan.


stack(s("hh*4"),
      s("bd mt sd ht").every(4, press)
     ).slow(2)

Source: `packages/core/pattern.mjs`.

### pressBy

**Call:** `.pressBy()`.

Like press, but allows you to specify the amount by which each
event is shifted. pressBy(0.5) is the same as press, while
pressBy(1/3) shifts each event by a third of its timespan.


stack(s("hh*4"),
      s("bd mt sd ht").pressBy("<0 0.5 0.25>")
     ).slow(2)

Source: `packages/core/pattern.mjs`.

### progNum

**Call:** `.progNum(program)`.

MIDI program number: Sends a MIDI program change message.

```js
note("c4").progNum(10).midichan(1).midi()
```

Source: `packages/core/controls.mjs`.

### psustain

**Call:** `.psustain(level)`.

Sustain level of the pitch envelope. `pattack`, `pdecay`, and `prelease` are the other times. The pitch envelope also needs `penv` if the pitch is going to move. Alias: `psus`.

```js
note("c3 eb3 g3").s("sawtooth").penv(12).psustain("<0 .5 1>").gain(0.15)
```

Source: `packages/core/controls.mjs`.

### pw

**Call:** `.pw(pulsewidth)`.

Controls the pulsewidth of the pulse oscillator

```js
note("{f a c e}%16").s("pulse").pw(".8:1:.2")
```

```js
n(run(8)).scale("D:pentatonic").s("pulse").pw("0 .75 .5 1")
```

Source: `packages/core/controls.mjs`.

### pwrate

**Call:** `.pwrate(rate)`. Alias: `pwr`.

Controls the lfo rate for the pulsewidth of the pulse oscillator

```js
n(run(8)).scale("D:pentatonic").s("pulse").pw("0.5").pwrate("<5 .1 25>").pwsweep("<0.3 .8>")
```

Source: `packages/core/controls.mjs`.

### pwsweep

**Call:** `.pwsweep(sweep)`. Alias: `pws`.

Controls the lfo sweep for the pulsewidth of the pulse oscillator

```js
n(run(8)).scale("D:pentatonic").s("pulse").pw("0.5").pwrate("<5 .1 25>").pwsweep("<0.3 .8>")
```

Source: `packages/core/controls.mjs`.
