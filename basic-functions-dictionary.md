# Strudel function dictionary

Use this dictionary alongside the [local setup guide](README.md). It covers core functions for making music in the browser editor, grouping related functions where their musical meaning is easier to understand together. The [full function dictionary](function-dictionary.md) is the alphabetical index of every registered function. Each example is a complete pattern; evaluate one code block at a time. Unless a block sets tempo, first evaluate `setcpm(120 / 4)`.

## Patterns and musical time

A pattern describes events in time. An event can carry a note, a sound name, amplitude, and effect settings. A function may create a pattern, transform its time or values, or attach sound controls. Chaining reads left to right, and order can matter: converting scale degrees to notes before transposing gives the transpose operation actual pitches to work on.

A **cycle** is Strudel's repeating time unit, not an intrinsic time signature. At 30 cycles per minute, each cycle lasts two seconds. If you count four beats in each cycle, that is 120 BPM in a one-bar 4/4 interpretation. If you count three beats per cycle, it is 90 BPM instead.

An **onset** is when an event starts. Its pattern duration is its span in musical time. Its audible duration also depends on the sound and envelope: a release tail can continue after the event span ends. **Pitch** determines how high a tone sounds; **timbre** is its tone color; **dynamics** concern amplitude and perceived loudness; **articulation** concerns how notes begin, sustain, and end.

### Mini notation is syntax inside strings

These symbols are not JavaScript functions. They build the pattern passed to functions such as `note` and `s`.

| Syntax | Meaning | Musical interpretation in a four-beat cycle |
| --- | --- | --- |
| `"c4 e4 g4 b4"` | Four equal sequential slots | Four quarter notes |
| `"c4 [e4 g4] b4 c5"` | Subdivide the second slot | Two eighth notes on beat two |
| `"c4 ~ g4 ~"` | `~` is a rest | Notes on beats one and three |
| `"c4*4"` | Repeat four times in the available span | Four regular attacks |
| `"<c4 e4 g4>"` | Choose successive alternatives on successive cycles | One long note per cycle, three-cycle phrase |
| `"[c4,e4,g4]"` | Stack simultaneous pitches | A C-major chord |
| `"c4(3,8)"` | Three Euclidean pulses across eight steps | Uneven gaps distributed as evenly as possible |

Brackets allocate time within their parent slot; adding notes inside brackets does not extend the cycle. Commas create simultaneity, while spaces create succession. This makes rhythm a matter of nested proportions.

## Function index

| Musical question | Functions |
| --- | --- |
| How fast is the whole piece? | [setcpm and setcps](#setcpm-and-setcps) |
| What pitch and instrument? | [note](#note), [s and sound](#s-and-sound), [n and scale](#n-and-scale), [transpose](#transpose) |
| How do I reshape rhythm? | [fast and slow](#fast-and-slow), [early and late](#early-and-late), [rev](#rev), [euclid](#euclid), [struct](#struct) |
| How do I combine and vary parts? | [stack](#stack), [cat](#cat), [lastOf](#lastof), [sometimes](#sometimes) |
| How do I shape the sound? | [gain](#gain), [attack decay sustain and release](#attack-decay-sustain-and-release), [lpf](#lpf) |
| How do I add space or motion? | [pan](#pan), [room](#room), [delay](#delay), [range](#range) |

## setcpm and setcps

**Calls:** `setcpm(cyclesPerMinute)` and `setcps(cyclesPerSecond)`. These set the editor's global scheduler tempo; they are not chained sound controls. Their relationship is `cpm = cps × 60`. For a chosen number of beats per cycle, use `cpm = BPM / beatsPerCycle`.

```js
setcpm(120 / 4)
note("c4*4").s("triangle").gain(0.2)
```

Here 30 cycles per minute equals 0.5 cycles per second. Four notes per cycle produce two attacks per second. **Listen:** change 120 to 90; every part slows together. **Pitfall:** `setcpm(120)` would make this pattern four times faster than intended. Strudel does not assume four beats per cycle for you.

Source: [REPL tempo controls](../../packages/core/repl.mjs).

## note

**Call:** `note(pitches)` or `pattern.note()`. Attach pitch information using note names with octaves, such as `c4`, `eb4`, and `fs4`, or MIDI note numbers. In the standard tuning, MIDI 69 is A4 at 440 Hz, and adding 12 MIDI units raises pitch by an octave.

```js
note("c4 eb4 g4 bb4").s("triangle").gain(0.2)
```

This outlines C minor seventh: root, minor third, perfect fifth, minor seventh. The notes occur successively, so it is an arpeggio. **Listen:** change the string to `"[c4,eb4,g4,bb4]"` to hear the same harmony as a chord. **Pitfall:** four notes separated by spaces are not a simultaneous chord. Numeric pitches are not scale degrees unless you explicitly map degrees with `scale`.

Source: [controls](../../packages/core/controls.mjs).

## s and sound

**Call:** `.s(name)`; `sound` is an alias. Select the sound source. Built-in oscillator names include `sine`, `triangle`, `sawtooth`, and `square`; sample names depend on loaded sample banks. `s(...)` can also create a sound pattern directly.

```js
note("c3 e3 g3 c4").s("<sine triangle sawtooth square>").gain(0.15)
```

The instrument changes each cycle. A sine emphasizes a single frequency; sawtooth and square waves have strong upper harmonics, giving filters more material to shape. **Listen:** compare brightness while keeping the notes fixed. **Pitfall:** selecting a pitched oscillator does not establish a scale, and naming a sample does not load a missing bank.

Source: [controls](../../packages/core/controls.mjs), [synth guide](../../website/src/pages/learn/synths.mdx).

## n and scale

**Calls:** `n(values).scale("root:scale")`. `n` is context-dependent: it can select sample indices, while `scale` interprets numeric values as scale degrees and maps them to pitches. Degrees are zero-based: in `C4:major`, 0 is C4, 1 is D4, and 2 is E4. Degree 7 reaches C5; negative degrees descend below the root.

```js
n("0 2 4 6").scale("C4:major").s("triangle").gain(0.2)
```

This outlines C major seventh (C, E, G, B). Change `major` to `minor` to obtain C, E-flat, G, B-flat. **Listen:** keep the degree contour unchanged and compare the harmony. **Pitfall:** degree 2 means the third scale note, not two semitones. Specify the octave for predictable register; this implementation defaults an unspecified scale root to octave 3. Scale names containing spaces use colons inside mini notation.

Source: [tonal scale implementation](../../packages/tonal/tonal.mjs), [controls](../../packages/core/controls.mjs).

## transpose

**Call:** `.transpose(semitonesOrInterval)`. Move pitches by a chromatic distance; numeric values count semitones, and interval strings such as `"5P"` describe a perfect fifth. Transposition preserves the interval relationships within the phrase.

```js
note("c4 e4 g4").transpose("<0 7>").s("triangle").gain(0.2)
```

Alternating cycles play a C-major and a G-major arpeggio. **Listen:** replace 7 with 12 to change register by an octave without changing pitch classes. **Pitfall:** chromatic transposition can move notes outside the original key. To write within a scale, work with degrees before mapping them through `scale`.

Source: [tonal functions](../../packages/tonal/tonal.mjs).

## fast and slow

**Calls:** `.fast(factor)` and `.slow(factor)`. For positive factors, `fast(2)` compresses time by two and `slow(2)` stretches it by two. These transform the selected pattern, while the global cycle clock remains unchanged. `fast(0.5)` corresponds to `slow(2)`.

```js
note("c4 e4 g4 b4").s("triangle").fast(2).gain(0.2)
```

Eight attacks now fit in a cycle instead of four. In a four-beat interpretation, the quarter-note line becomes eighth notes. **Listen:** compare factors 1, 2, and 0.5 while counting the same pulse. **Pitfall:** faster note events do not raise oscillator pitch; this is different from increasing sample playback speed. Fixed envelope times in seconds may overlap when events become denser.

Source: [pattern time transforms](../../packages/core/pattern.mjs).

## early and late

**Calls:** `.early(cycles)` and `.late(cycles)`. Shift a pattern earlier or later by a fraction of a cycle. Events wrap across cycle boundaries, so this is a phase shift of a repeating pattern.

```js
stack(
  note("c3*4").s("sine").gain(0.15),
  note("g4*4").s("triangle").late(1/8).gain(0.12)
)
```

At four beats per cycle, `1/8` cycle is half a beat. The upper line lands between the lower line's notes, creating offbeats. **Listen:** compare `late(1/8)` with `late(1/4)`; the latter aligns to another beat of this evenly repeating pattern. **Pitfall:** the argument is cycles, not seconds. Moving every onset equally does not create swing, which requires unequal spacing between subdivisions.

Source: [pattern time transforms](../../packages/core/pattern.mjs).

## rev

**Call:** `.rev()`. Reverse the pattern in each cycle, reflecting its event timing as well as its order. This is a musical retrograde transformation.

```js
note("c4 [e4 g4] b4 c5").s("triangle").rev().gain(0.2)
```

The ascending figure reverses, including the placement of its subdivision. **Listen:** remove and restore `rev` to compare the rhythmic contour. **Pitfall:** this does not reverse the audio waveform or sample itself, and reversal within each cycle is not the same as reversing an entire multi-cycle composition.

Source: [rev implementation](../../packages/core/pattern.mjs).

## euclid

**Call:** `.euclid(pulses, steps)`. Distribute a number of attacks across a grid as evenly as possible. Start with integer values satisfying `0 < pulses <= steps`. When steps cannot be divided evenly by pulses, the gaps differ, giving a balanced but nonuniform rhythm.

```js
note("c4").s("triangle").euclid(3, 8).decay(0.08).sustain(0).gain(0.2)
```

Three attacks occupy an eight-step cycle. Counting eight equal subdivisions helps reveal the longer and shorter gaps. **Listen:** compare `(3, 8)`, `(5, 8)`, and `(4, 8)`. **Pitfall:** eight steps do not inherently mean eight beats; in a four-beat cycle they can represent eighth notes. Equal distribution is a construction method, not a complete description of a cultural groove or its performance accents.

Source: [Euclidean rhythms](../../packages/core/euclid.mjs).

## struct

**Call:** `.struct(binaryPattern)`. Give a pattern the rhythmic structure of another pattern. True/1 slots create events; false/0 slots leave gaps. Using a single sustained value as the source makes this relationship easy to hear.

```js
note("c4").s("triangle").struct("1 0 1 1 0 0 1 0").gain(0.2)
```

This separates a rhythm's attack grid from its pitch and instrument. **Listen:** change only the zeros and ones, then keep the rhythm and change `c4` to `g4`. **Pitfall:** with a multi-note source, interaction with the source's values and timing is more involved than simply consuming the next note from a list. Start with a single value when designing a beat.

Source: [pattern structure](../../packages/core/pattern.mjs).

## stack

**Call:** `stack(patternA, patternB, ...)`. Combine patterns simultaneously. Each part keeps its own temporal structure, so parts can have different subdivisions or repetition lengths.

```js
stack(
  note("c3 g3").s("sine").gain(0.15),
  note("c4 e4 g4 b4").s("triangle").gain(0.12)
)
```

The lower voice gives a slower harmonic foundation and the upper voice outlines a melody. **Listen:** apply `.fast(2)` only to the upper part, then apply it after the closing `stack(...)` instead. The second placement transforms both parts. **Pitfall:** layered amplitudes add; give each part room in the mix. A control after `stack` applies to the combined pattern and can replace values assigned inside individual parts.

Source: [stack](../../packages/core/pattern.mjs).

## cat

**Call:** `cat(patternA, patternB, ...)`. Present successive patterns on successive cycles. With two one-cycle phrases, the resulting form repeats every two cycles.

```js
cat(
  note("c4 e4 g4 e4"),
  note("f4 a4 c5 a4")
).s("triangle").gain(0.2)
```

This alternates C-major and F-major material, a simple I–IV harmonic movement in C major. **Listen:** add a third pattern `note("g4 b4 d5 b4")` to include V. **Pitfall:** `cat` does not squeeze all its arguments into a single cycle; use a faster composition when that is your intent.

Source: [cat](../../packages/core/pattern.mjs).

## lastOf

**Call:** `.lastOf(cycleCount, transform)`. Apply a transformation on the last cycle of each group. The callback receives a pattern and must return its transformed version. `p => p.fast(2)` is a JavaScript function that does exactly that.

```js
note("c4 e4 g4 b4").s("triangle").lastOf(4, p => p.fast(2)).gain(0.2)
```

Three regular cycles are followed by a denser fourth cycle. This creates a predictable fill and articulates a four-bar phrase if one cycle represents one bar. **Listen:** count four cycles and hear the return to the original density. **Pitfall:** the grouping follows the running cycle clock; evaluating midway through playback need not begin a new four-cycle group.

Source: [conditional pattern transforms](../../packages/core/pattern.mjs).

## sometimes

**Call:** `.sometimes(transform)`. Probabilistically apply a transformation, using probability 0.5. The related `.sometimesBy(probability, transform)` lets you choose a probability between 0 and 1. This is pattern-based variation; do not assume that every use behaves as one independent coin toss for a whole bar.

```js
note("c4 e4 g4 b4").s("triangle").sometimes(p => p.transpose(12)).gain(0.2)
```

Octave displacement keeps the pitch classes while varying register. **Listen:** compare this with `lastOf(4, p => p.transpose(12))`; one gives probabilistic variation, the other a regular formal marker. **Pitfall:** Strudel's randomness is tied to pattern time, so repeated queries can be reproducible. “Sometimes” does not promise a particular number of changes in a short listening window.

Source: [random transforms](../../packages/core/signal.mjs).

## gain

**Call:** `.gain(amplitude)`. Scale a sound's amplitude with a number or pattern of numbers. Zero silences it; 1 represents unity gain, not a guarantee of a safe or constant perceived loudness.

```js
note("c4*4").s("triangle").gain("0.25 0.1 0.16 0.1")
```

The stronger first note establishes a downbeat; the third receives a secondary accent. This is a dynamic pattern even though the pitch and onset spacing are constant. **Listen:** move the largest value to the second slot and notice the shifted emphasis. **Pitfall:** halving linear amplitude does not necessarily sound half as loud. Timbre, register, layering, and playback level also affect perceived loudness.

Source: [gain control](../../packages/core/controls.mjs).

## attack decay sustain and release

**Calls:** `.attack(seconds)`, `.decay(seconds)`, `.sustain(level)`, `.release(seconds)`. Together these shape the amplitude envelope: rise from silence, fall from the peak, maintain a level, then fade after release. Sustain is a level, not a duration.

```js
note("c4 e4 g4 b4").s("sawtooth")
  .attack(0.005).decay(0.12).sustain(0).release(0.08).gain(0.15)
```

With sustain at zero, the tone decays to silence, giving a plucked articulation. A sustained alternative is:

```js
note("[c4,e4,g4]").s("triangle")
  .attack(0.4).decay(0.2).sustain(0.6).release(0.5).gain(0.12)
```

The chord swells and leaves a tail. **Listen:** change attack alone, then release alone; the first softens the beginning, the second extends the ending. **Pitfall:** these time values are in seconds and do not automatically scale with tempo. Long attacks on short events can prevent a sound from reaching its peak, and long releases can overlap following notes. Sound engines and sample playback can impose further duration behavior.

Source: [envelope controls](../../packages/core/controls.mjs), [synth guide](../../website/src/pages/learn/synths.mdx).

## lpf

**Call:** `.lpf(frequencyHz)`; `cutoff` is an alias. A low-pass filter attenuates frequencies above its cutoff. It mainly changes brightness, not the note identity assigned by `note`.

```js
note("c3 e3 g3 b3").s("sawtooth").lpf("<400 1000 4000>").gain(0.15)
```

The same phrase becomes successively brighter across three cycles. Sawtooth has upper harmonics that make the effect easy to hear. **Listen:** replace sawtooth with sine; a pure tone has much less harmonic content for the filter to remove. **Pitfall:** a cutoff below the fundamental can make the entire sound quiet. Hertz is a frequency unit, not a brightness percentage.

Source: [filter controls](../../packages/core/controls.mjs).

## pan

**Call:** `.pan(position)`. Place audio across the stereo field: 0 is left, 0.5 center, 1 right.

```js
note("c4 e4 g4 b4").s("triangle").pan("0 0.33 0.67 1").gain(0.2)
```

Successive notes move from left to right. Spatial separation can help distinguish simultaneous voices. **Listen:** compare the pattern with `.pan(0.5)` using stereo speakers or headphones. **Pitfall:** a mono output can conceal this movement; panning does not itself create echo or reverberation.

Source: [pan control](../../packages/core/controls.mjs).

## room

**Call:** `.room(level)`. Set the reverb send level. Reverb produces a dense tail of reflections and can suggest a shared acoustic space. Related controls such as `roomsize` shape the space; the `room` argument itself is not a measurement in meters.

```js
note("c4 ~ g4 ~").s("triangle").decay(0.1).sustain(0).room(0.3).gain(0.2)
```

The rests expose the tail, making it easier to hear the effect. **Listen:** compare room levels 0 and 0.3. **Pitfall:** heavy reverb can blur rhythmic articulation. This checkout tags reverb as an orbit effect, so routing matters when several parts share an effects bus; do not assume every part has an entirely independent room processor.

Source: [reverb controls](../../packages/core/controls.mjs).

## delay

**Calls:** `.delay(level)`, `.delaytime(seconds)`, `.delayfeedback(amount)`. Set the echo send level, the interval between repeats, and how much delayed sound feeds back into the delay. Begin with feedback well below 1.

```js
setcpm(120 / 4)
note("c4 ~ ~ ~").s("triangle").decay(0.08).sustain(0)
  .delay(0.3).delaytime(0.25).delayfeedback(0.3).gain(0.2)
```

At 120 BPM, one beat lasts 0.5 seconds, so a 0.25-second delay produces eighth-note spacing. **Listen:** use 0.375 seconds for dotted eighth notes. **Pitfall:** explicit `delaytime` values are in seconds; changing the tempo does not preserve this rhythmic relationship. Feedback controls repeat persistence, not note density in the source pattern.

Source: [delay controls](../../packages/core/controls.mjs).

## range

**Call:** `signal.range(min, max)`. Map a signal's normalized values to a useful parameter range. `sine` is a cyclic control signal; `.slow(4)` stretches its oscillation over four cycles.

```js
note("c3*8").s("sawtooth")
  .lpf(sine.range(300, 3000).slow(4)).gain(0.15)
```

The repeated notes become brighter and darker over a longer phrase. This is low-frequency modulation of timbre. **Listen:** change `slow(4)` to `slow(8)` to lengthen the sweep. **Pitfall:** `sine` here is a control pattern, whereas `.s("sine")` selects an audible oscillator. Pattern controls are generally sampled at event times; do not assume this expression continuously sweeps a filter throughout a single held note.

Source: [signals](../../packages/core/signal.mjs), [signal guide](../../website/src/pages/learn/signals.mdx).

## Put the functions together

This oscillator-only sketch combines a bass foundation with a scale-based melody. It needs no drum sample bank.

```js
setcpm(110 / 4)
stack(
  note("c2 ~ g2 ~").s("sine")
    .attack(0.01).decay(0.18).sustain(0).release(0.1).gain(0.22),
  n("0 2 4 6 4 2 1 2").scale("C4:minor").s("triangle")
    .lastOf(4, p => p.fast(2))
    .attack(0.01).decay(0.12).sustain(0).release(0.08)
    .pan(0.6).gain(0.12)
)
```

First identify the bass pulse. Then count the eight melody attacks per regular cycle. Finally hear the fourth-cycle fill. Change the scale to major, keep the rhythm unchanged, and describe the altered intervals. Add reverb only after you can hear the phrase structure clearly.

## Extend the dictionary

For each new entry, record the exact name and aliases, signature, parameter units, pattern behavior, musical interpretation, complete playable example, listening exercise, common mistake, related functions, and source link. Check semantics against this checkout's implementation and adjacent tests. Keep advanced topics such as sample slicing, chord voicings, MIDI, and microtonality in separate groups as the reference grows.

For broader coverage, use the [existing learn pages](../../website/src/pages/learn) and the source JSDoc. `pnpm jsdoc-json` generates the machine-readable API documentation used by the website; it complements these listening-oriented explanations.
