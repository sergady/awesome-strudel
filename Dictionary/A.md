### A

- `absoluteOrientationAlpha`
- `absoluteOrientationBeta`
- `absoluteOrientationGamma`
- `absoluteOrientationX` — alias of `absoluteOrientationBeta`
- `absoluteOrientationY` — alias of `absoluteOrientationGamma`
- `absoluteOrientationZ` — alias of `absoluteOrientationAlpha`
- `absOriA` — alias of `absoluteOrientationAlpha`
- `absOriB` — alias of `absoluteOrientationBeta`
- `absOriG` — alias of `absoluteOrientationGamma`
- `absOriX` — alias of `absoluteOrientationBeta`
- `absOriY` — alias of `absoluteOrientationGamma`
- `absOriZ` — alias of `absoluteOrientationAlpha`
- `accelerate`
- `accelerationX`
- `accelerationY`
- `accelerationZ`
- `accX` — alias of `accelerationX`
- `accY` — alias of `accelerationY`
- `accZ` — alias of `accelerationZ`
- `activeLabel`
- `ad`
- `add`
- `addVoicings`
- `adsr`
- `almostAlways`
- `almostNever`
- `always`
- `amp`
- `analyze`
- `anchor`
- `and`
- `apply`
- `applyN`
- `ar`
- `arp`
- `arpWith`
- `as`
- `asym`
- `att` — alias of `attack`
- `attack`

## Entries

### absoluteOrientationAlpha

**Call:** `absoluteOrientationAlpha`, a pattern. Aliases: `absOriA`, `absOriZ`, `absoluteOrientationZ`.

The device's absolute-orientation alpha axis, scaled from 0 to 1. This comes from `@strudel/motion`, which the default editor prebake does not load.

```js
n(absoluteOrientationAlpha.segment(4).range(0, 7)).scale("C:minor")
```

**Musical:** tilting or rotating the device chooses scale degrees. `segment(4)` takes four samples per cycle, so the melody moves in steps. `range(0, 7)` maps the sensor onto one octave of scale degrees.

Source: `packages/motion/motion.mjs`.

### absoluteOrientationBeta

**Call:** `absoluteOrientationBeta`, a pattern. Aliases: `absOriB`, `absOriX`, `absoluteOrientationX`.

The device's absolute-orientation beta axis, scaled from 0 to 1. Requires `@strudel/motion`.

```js
n(absoluteOrientationBeta.segment(4).range(0, 7)).scale("C:minor")
```

**Musical:** a different orientation axis drives the same kind of stepped melody as `absoluteOrientationAlpha`. Holding the device still holds the pitch; moving it along this axis walks through the scale.

Source: `packages/motion/motion.mjs`.

### absoluteOrientationGamma

**Call:** `absoluteOrientationGamma`, a pattern. Aliases: `absOriG`, `absOriY`, `absoluteOrientationY`.

The device's absolute-orientation gamma axis, scaled from 0 to 1. Requires `@strudel/motion`.

```js
n(absoluteOrientationGamma.segment(4).range(0, 7)).scale("C:minor")
```

**Musical:** the gamma axis is a third physical direction for the same degree-picking melody. Compare it with alpha and beta by rotating the device in one direction at a time.

Source: `packages/motion/motion.mjs`.

### accelerate

**Call:** `.accelerate(amount)`.

A control that speeds up or slows down a sample while it plays. The source marks it `@superdirtOnly`, and the example sends audio with `.osc()`.

```js
s("sax").accelerate("<0 1 2 4 8 16>").slow(2).osc()
```

**Musical:** each cycle ramps the sample's playback speed by a larger amount, so the tone slides upward as the sample plays. `slow(2)` gives the ramp two cycles to speak. The local browser engine does not read this control; sample playback speed there is `speed`.

Source: `packages/core/controls.mjs`.

### accelerationX

**Call:** `accelerationX`, a pattern. Alias: `accX`.

The accelerometer x-axis, scaled from 0 to 1. Requires `@strudel/motion`.

```js
n(accelerationX.segment(4).range(0, 7)).scale("C:minor")
```

**Musical:** shaking or moving the device along this axis changes the scale degree four times per cycle. A still device holds a steady pitch.

Source: `packages/motion/motion.mjs`.

### accelerationY

**Call:** `accelerationY`, a pattern. Alias: `accY`.

The accelerometer y-axis, scaled from 0 to 1. Requires `@strudel/motion`.

```js
n(accelerationY.segment(4).range(0, 7)).scale("C:minor")
```

**Musical:** motion on the y-axis picks the melody. It is the same mapping as `accelerationX`, on another physical axis.

Source: `packages/motion/motion.mjs`.

### accelerationZ

**Call:** `accelerationZ`, a pattern. Alias: `accZ`.

The accelerometer z-axis, scaled from 0 to 1. Requires `@strudel/motion`.

```js
n(accelerationZ.segment(4).range(0, 7)).scale("C:minor")
```

**Musical:** motion on the z-axis, often toward and away from the floor when the device is flat, chooses the scale degree.

Source: `packages/motion/motion.mjs`.

### activeLabel

**Call:** `.activeLabel(text)`.

Sets the text drawn for an event on the piano roll while that event is sounding. `label` is the text used when the event is not active.

```js
note("c4 e4 g4").s("triangle").label("resting").activeLabel("now").gain(0.2)
```

**Musical:** the sound is unchanged. The roll shows "now" on the note that is currently playing and "resting" on the others, which makes the downbeat of a phrase easier to see.

Source: `packages/core/controls.mjs`, `packages/draw/pianoroll.mjs`.

### ad

**Call:** `.ad(attack, decay)`. Times are in seconds. One value sets both attack and decay. A mini-notation colon builds the pair, as in `.ad(".01:.12")`.

Attack is how long the amplitude takes to rise. Decay is how long it then falls.

```js
note("c4 e4 g4 b4").s("sawtooth").ad(".01:.12").sustain(0).gain(0.15)
```

**Musical:** a short attack and a longer decay, with sustain at 0, speaks like a pluck: the tone is present immediately and then dies. Lengthen only the decay and the same pitches ring longer. These times are in seconds, so they do not follow tempo.

Source: `packages/core/controls.mjs`. Longer envelope notes: [basic dictionary](basic-functions-dictionary.md#attack-decay-sustain-and-release).

### add

**Call:** `.add(amount)`.

Adds a number to each value. Note names are handled as MIDI numbers, so adding 12 raises them by an octave.

```js
n("0 2 4".add("<0 3 4 0>")).scale("C:major").s("triangle").gain(0.2)
```

**Musical:** the same 0–2–4 triad shape sits on a moving root. The added amounts 0, 3, 4, 0 step the chord through scale degrees, a diatonic shift. On notes, `note("c3 e3 g3".add("<0 5 7 0>"))` moves that triad by semitones instead of scale degrees.

Source: `packages/core/pattern.mjs`.

### addVoicings

**Call:** `addVoicings(name, dictionary, range)`.

Registers a named dictionary of chord voicings. Each chord symbol maps to one or more stacks of intervals, such as `"3M 7m 9M"`. `range` is the lowest and highest note the voicing may use. The default range is `F3` to `A4`.

```js
addVoicings('lesson', {
  '^7': ['3M 7M 10M 14M'],
  m7: ['3m 7m 10m 14m']
}, ['C3', 'C5'])
"<C^7 Dm7>".voicings('lesson').note().s("triangle").gain(0.15)
```

**Musical:** the chord symbol chooses the harmony, and the dictionary chooses which notes of that chord are actually played. A close voicing sits in a narrow register; a wider interval list spreads the same chord. The range stops the voicing from jumping outside the band you set.

Source: `packages/tonal/voicings.mjs`.

### adsr

**Call:** `.adsr(attack, decay, sustain, release)`. Attack, decay, and release are seconds. Sustain is a level from 0 to 1.

Sets all four amplitude-envelope stages at once. The colon form packs them into one value.

```js
note("[c3 bb2 f3 eb3]*2").s("sawtooth").lpf(600).adsr(".1:.1:.5:.2").gain(0.15)
```

**Musical:** each note takes a tenth of a second to bloom, falls slightly, holds at half amplitude, then fades for a fifth of a second. Raise the attack and the line becomes a swell. Set sustain to 0 and the notes become plucks. The pitch pattern is unchanged.

Source: `packages/core/controls.mjs`. Longer envelope notes: [basic dictionary](basic-functions-dictionary.md#attack-decay-sustain-and-release).

### almostAlways

**Call:** `.almostAlways(transform)`.

Applies the transform with probability 0.9. It is `sometimesBy(0.9, fn)`.

```js
note("c4*8").s("triangle").almostAlways(x => x.transpose(12)).gain(0.2)
```

**Musical:** nearly every note jumps up an octave. About one event in ten stays in the written register, a small irregular dip. The eight attacks per cycle stay in place.

Source: `packages/core/signal.mjs`.

### almostNever

**Call:** `.almostNever(transform)`.

Applies the transform with probability 0.1. It is `sometimesBy(0.1, fn)`.

```js
note("c4*8").s("triangle").almostNever(x => x.transpose(12)).gain(0.2)
```

**Musical:** the notes mostly stay on C4. Occasionally one sounds an octave higher, a rare register change on a steady pulse.

Source: `packages/core/signal.mjs`.

### always

**Call:** `.always(transform)`.

Applies the transform every time. It is `sometimesBy(1, fn)`.

```js
note("c4*8").s("triangle").always(x => x.transpose(12)).gain(0.2)
```

**Musical:** every note sounds an octave higher. There is no occasional original pitch, so the line is a steady C5 pulse. The written `c4` is the input; the transform moves all of it.

Source: `packages/core/signal.mjs`.

### amp

**Call:** `.amp(amount)`.

An amplitude control marked `@superdirtOnly` in the source. The comment describes it as gain, with a linear amount.

```js
s("bd*8").amp(".1*2 .5 .1*2 .5 .1 .5").osc()
```

**Musical:** the kick accents follow the numbers: quiet, quiet, loud, and so on. The rhythm stays eight hits per cycle; only the loudness pattern moves the beat. The local browser engine reads `gain` for this kind of accent.

Source: `packages/core/controls.mjs`.

### analyze

**Call:** `.analyze(amount)`.

Send amount, from 0 to 1, into an analyser node used by the scope. It does not retune or filter the synth.

```js
note("c3 e3 g3").s("sawtooth").analyze(1).gain(0.15)
```

**Musical:** the phrase sounds the same at 0 and at 1. The control feeds the visual scope so you can see the waveform of the part you are hearing. `fft` sets that analyser's size.

Source: `packages/core/controls.mjs`, `packages/superdough/superdough.mjs`.

### anchor

**Call:** `.anchor(noteName)`.

The note that a voicing or scale aligns to.

```js
n("0 .. 7").anchor("<c4 g4 c5 g5>").scale("C:major").s("triangle").gain(0.2)
```

**Musical:** the scale degrees stay 0 through 7, but the register they sit in follows the anchor. Moving the anchor from C4 to C5 lifts the same melody by an octave. With chords, `anchor("<c4 g4 c5 g5>").chord("C").voicing()` keeps a C chord and changes how high its top note is allowed to sit.

Source: `packages/core/controls.mjs`.

### and

**Call:** `.and(other)`.

Combines two patterns with JavaScript `&&`. When the left value is truthy, the result is the right value. When the left value is falsy, such as 0, the result is that falsy value.

```js
n("1".and("0 2 4 7")).scale("C4:major").s("triangle").gain(0.2)
```

**Musical:** a left-hand 1 lets the degrees 0, 2, 4, 7 through, a major seventh arpeggio. Replace `1` with `0` and every value becomes 0, so the line collapses to the root. It is a gate for pattern values, not a simultaneous harmony.

Source: `packages/core/pattern.mjs`.

### apply

**Call:** `.apply(func)`.

Calls `func` with the current pattern and uses whatever pattern it returns.

```js
note("c4 e4 g4").apply(p => p.transpose(7)).s("triangle").gain(0.2)
```

**Musical:** the function moves every note up 7 semitones, a perfect fifth, so the C major triad becomes a G major triad. The rhythm stays. `apply` is the place in a chain where your own function receives the pattern and returns the next one.

Source: `packages/core/pattern.mjs`.

### applyN

**Call:** `.applyN(times, func)`.

Runs `func` on the pattern `times` times. Each pass receives the previous result.

```js
note("c4 e4 g4").s("triangle").applyN(2, p => p.fast(2)).gain(0.2)
```

**Musical:** one `fast(2)` fits the phrase into the cycle twice. The second pass doubles it again, so the three notes speak four times as often. Repeating a transpose instead, `.applyN(3, p => p.transpose(1))`, walks the same line up three semitones, a minor third.

Source: `packages/core/pattern.mjs`.

### ar

**Call:** `.ar(attack, release)`. Times are in seconds. One value sets both. A colon pair sets them separately, as in `.ar(".01:.2")`.

Sets attack and release on the amplitude envelope.

```js
note("c4 e4 g4").s("triangle").ar(".01:.3").sustain(0.6).gain(0.2)
```

**Musical:** the note starts quickly and keeps a tail of three tenths of a second after the event. A longer release makes the pitches blur into each other. A longer attack softens the start of each note.

Source: `packages/core/controls.mjs`.

### arp

**Call:** `.arp(indices)`.

Picks notes out of a stacked chord by index. Index 0 is the first stacked value. Indices wrap with modulo.

```js
note("<[c,eb,g]!2 [c,f,ab] [d,f,ab]>").arp("0 [0,2] 1 [0,2]").s("triangle").gain(0.2)
```

**Musical:** each bracket is a chord. The arp pattern decides which chord tones speak: the bottom note, then bottom and top together, then the middle note. You hear the harmony as a line instead of a block. `[0,2]` on a triad is the root and the fifth if the stack is written root, third, fifth.

Source: `packages/core/pattern.mjs`.

### arpWith

**Call:** `.arpWith(func)`.

Like `arp`, but `func` receives the stacked events and returns the ones to play.

```js
note("<[c,eb,g]!2 [c,f,ab] [d,f,ab]>").arpWith(haps => haps[2]).s("triangle").gain(0.2)
```

**Musical:** index 2 is the top note of each triad, so the line follows the highest voice of a changing chord: G, then A-flat, then A-flat. The lower chord tones stay in the stack and are not heard.

Source: `packages/core/pattern.mjs`.

### as

**Call:** `.as(mapping)`.

Assigns colon-separated columns of a pattern to control names. In mini notation, `c:.5` is the array `["c", 0.5]`, and `"note:clip"` is the array `["note", "clip"]`.

```js
"c4:.5 e4:1 g4:.25".as("note:clip").s("triangle").gain(0.2)
```

**Musical:** pitch and clip travel in one pattern. Clip 1 holds the event for its full span; 0.25 keeps a quarter of that span, a shorter articulation on the same pitch. The rhythm of the three notes stays even while their lengths change.

Source: `packages/core/controls.mjs`.

### asym

**Call:** `.asym(amount)` or `.asym("amount:postgain")`.

Asymmetrical diode distortion. A single number is the drive; post-gain defaults to 1. The negative half of the waveform is not shaped by the input the way the positive half is, so the wave becomes lopsided. Quiet signals stay closer to clean.

```js
note("c3 eb3 g3 bb3").s("sawtooth").asym(4).gain(0.12)
```

**Musical:** the minor chord gains a rasp and extra harmonics. Compare `.asym(0)` with `.asym(4)` on a sawtooth, which already has harmonics for the shaper to bend. Keep `gain` low; distortion raises the harshness you hear.

Source: `packages/core/pattern.mjs`, `packages/superdough/helpers.mjs`.

### attack

**Call:** `.attack(seconds)`. Alias: `att`.

How long the amplitude takes to rise from silence to its peak after the onset.

```js
note("c3 e3 f3 g3").s("sawtooth").attack("<0 .1 .5>").decay(0.1).sustain(0).gain(0.15)
```

**Musical:** 0 starts the note at once. 0.1 softens the attack. 0.5 makes a swell, and on a short event the tone may never reach full loudness. The pitches stay the same; only the start of each note changes.

Source: `packages/core/controls.mjs`. Longer listening notes: [basic dictionary](basic-functions-dictionary.md#attack-decay-sustain-and-release).
