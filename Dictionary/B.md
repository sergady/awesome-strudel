### B

- `band`
- `bandf`
- `bandq`
- `bank`
- `base`
- `bb` — alias of `byteBeatExpression`
- `bbexpr` — alias of `byteBeatExpression`
- `bbst` — alias of `byteBeatStartTime`
- `beat`
- `begin`
- `berlin`
- `bgain` — alias of `busgain`
- `binary`
- `binaryL`
- `binaryN`
- `binaryNL`
- `binshift`
- `bite`
- `bjork`
- `blshift`
- `bmod`
- `bor`
- `bp` — alias of `bpf`
- `bpa` — alias of `bpattack`
- `bpattack`
- `bpdc`
- `bpdecay`
- `bpdepth`
- `bpdepthfreq` — alias of `bpdepthfrequency`
- `bpdepthfrequency`
- `bpe` — alias of `bpenv`
- `bpenv`
- `bpf`
- `bpq`
- `bpr` — alias of `bprelease`
- `bprate`
- `bprelease`
- `bps` — alias of `bpsustain`
- `bpshape`
- `bpskew`
- `bpsustain`
- `bpsync`
- `brak`
- `brand`
- `brandBy`
- `brshift`
- `bus`
- `busgain`
- `bxor`
- `bypass`
- `byteBeatExpression`
- `byteBeatStartTime`

## Entries

### band

**Call:** `.band(mask)`.

Bitwise AND of each number with the mask: `a & b`.

```js
n("0 1 2 3 4 5 6 7".band(5)).scale("C4:major").s("triangle").gain(0.2)
```

**Musical:** 5 is binary `101`, so only those bits survive. The eight degrees collapse onto 0, 1, 4, and 5, a smaller set of pitches repeating inside the bar. The rhythm of eight notes stays even.

Source: `packages/core/pattern.mjs`.

### bandf

**Call:** `.bandf(frequencyHz)`. Same method as `bpf` and `bp`.

Center frequency of the band-pass filter, in hertz. A colon value can also set resonance and envelope depth, because this control is registered as the triple `bandf:bandq:bpenv`.

```js
note("c3 e3 g3 b3").s("sawtooth").bandf("<400 800 1600 3200>").gain(0.12)
```

**Musical:** a band-pass keeps a band around the center and turns down what is far above and below it. The same arpeggio gets thinner and more whistling as the center rises. Sawtooth has harmonics for the filter to pick through. A center near the note's fundamental keeps that pitch clear; a center far from it leaves a faint slice of the spectrum.

Source: `packages/core/controls.mjs`.

### bandq

**Call:** `.bandq(q)`. Same method as `bpq`.

Resonance (Q) of the band-pass filter. Higher Q makes the passed band narrower.

```js
note("c3*4").s("sawtooth").bpf(800).bandq("<0 1 3 8>").gain(0.12)
```

**Musical:** the pitch stays on C3 and the center stays at 800 Hz. Raising Q makes the tone honk, as if one harmonic is being singled out. At 0 the band is wide and the sawtooth stays fuller.

Source: `packages/core/controls.mjs`.

### bank

**Call:** `.bank(name)`.

Prepends `name` and an underscore to each sound in `s`. `bank("RolandTR909")` turns `bd` into `RolandTR909_bd`.

```js
s("bd sd [~ bd] sd").bank("RolandTR909")
```

**Musical:** the rhythm is unchanged. The bank swaps the drum kit, so the same kick-snare pattern speaks with a different machine's samples. The named bank has to be loaded; the prefix does not fetch it.

Source: `packages/core/controls.mjs`.

### base

**Call:** `base(number, radix, digits)`.

Turns a number into the sequence of its digits in the given base. `radix` defaults to 10. `digits` defaults to 0, which keeps every digit; a positive count keeps that many digits from the right.

```js
note(base("7175 543", 10, 3)).scale("C:major").s("sawtooth").gain(0.15)
```

**Musical:** 7175 in base 10 is the digits 7, 1, 7, 5, and the limit 3 keeps 1, 7, 5. Then 543 keeps 5, 4, 3. Those digits become scale degrees, so the decimal writing of the number is the melody. Base 2 would spell the same numbers as binary degrees instead.

Source: `packages/core/pattern.mjs`.

### beat

**Call:** `.beat(steps, divisions)`.

Places the pattern on chosen steps of a grid. `divisions` is how many equal slots the cycle is cut into.

```js
s("bd").beat("0,7,10", 16)
```

**Musical:** a 16-step grid is a bar of sixteenth notes if you count four beats. Hits on steps 0, 7, and 10 are the downbeat, the "and" of beat 2, and a later offbeat. `s("sd").beat("4,12", 16)` puts the snare on beats 2 and 4 of that same grid. The sound is whatever pattern you called `beat` on; the numbers only choose the attacks.

Source: `packages/core/pattern.mjs`.

### begin

**Call:** `.begin(amount)`.

Skips into each sample. 0 starts at the beginning. 1 is the end of the sample, so 0.25 drops the first quarter.

```js
s("bd*4").begin("<0 .25 .5 .75>")
```

**Musical:** later start points cut off the attack of the hit. The kick loses its click and you hear more of the body or the tail. The four attacks per cycle stay in time; only the audio inside each hit moves. This follows the sample, so an oscillator with no sample body will not show the same skip.

Source: `packages/core/controls.mjs`.

### berlin

**Call:** `berlin`, a pattern from 0 to 1.

A noise signal made of straight rising ramps. Each ramp runs from a random height to a higher one, then the next ramp starts somewhere new. `.fast(4)` fits four ramps into a cycle.

```js
n("0!16".add(berlin.fast(4).mul(14))).scale("D:minor").s("triangle").gain(0.2)
```

**Musical:** sixteen equal notes climb in jagged lines and then jump to a new starting degree. The contour is a sawtooth of pitch, not a smooth wobble. `mul(14)` sets how many scale degrees the climb can cover.

Source: `packages/core/signal.mjs`.

### binary

**Call:** `binary(number)`.

Spreads the bits of a number across a cycle, most significant bit first. The pattern is only as long as the number needs.

```js
note("c4").s("triangle").struct(binary(5)).gain(0.2)
```

**Musical:** 5 is binary `101`, so the cycle is hit, rest, hit. The pitch stays on C4. Change the number and the rhythm changes, because the bits are the attacks. 5 and 2 (`10`) are different lengths; `binaryN` keeps a fixed bar length.

Source: `packages/core/signal.mjs`.

### binaryL

**Call:** `binaryL(number)`.

The bits of a number as one list, most significant bit first. The list is only as long as the number needs. `binary` spreads those bits in time; this keeps them together as one value, which `partials` can read as harmonic on/off switches.

```js
s("sawtooth").note("c3").partials(binaryL(21)).gain(0.15)
```

**Musical:** 21 is `10101`. Those five flags turn harmonics on, off, on, off, on, so the timbre is a hollow stack instead of a full sawtooth. The pitch stays C3. A different number is a different spectrum.

Source: `packages/core/signal.mjs`.

### binaryN

**Call:** `binaryN(number, bits)`.

Like `binary`, padded or trimmed to a fixed number of bits. `bits` defaults to 16.

```js
note("g4").s("triangle").struct(binaryN(5, 8)).gain(0.2)
```

**Musical:** 5 padded to 8 bits is `00000101`, eight equal steps with attacks only near the end of the bar. The grid stays eight steps when you change the number, so rhythms of different density still share one bar length.

Source: `packages/core/signal.mjs`.

### binaryNL

**Call:** `binaryNL(number, bits)`.

Like `binaryL`, padded or trimmed to a fixed number of bits. `bits` defaults to 16.

```js
s("sawtooth").note("c3").partials(binaryNL(21, 8)).gain(0.15)
```

**Musical:** 21 padded to 8 bits is `00010101`. The extra leading zeros mute the first harmonics, and the later ones still blink on and off. The pitch stays C3 while the spectrum gets a fixed width you can compare from number to number.

Source: `packages/core/signal.mjs`.

### binshift

**Call:** `.binshift(amount)`.

A registered control with no description and no reader in this checkout's browser synth. It sits with other SuperDirt spectral controls such as `hbrick` and `lbrick`.

```js
note("c3 e3 g3").s("sawtooth").binshift("<0 1 2>").gain(0.12)
```

**Musical:** in the local browser engine this call does not retune or filter the chord. The pitches and the sawtooth stay as written. Treat it as a control name reserved for a spectral bin shift, not as a tone you can hear here.

Source: `packages/core/controls.mjs`.

### bite

**Call:** `.bite(slices, order)`.

Cuts the pattern into `slices` equal pieces and plays the pieces named by `order`. This slices the pattern in time. It does not slice an audio sample.

```js
note("c4 d4 e4 f4 g4 a4 b4 c5").s("triangle").bite(4, "3 2 1 0").gain(0.2)
```

**Musical:** eight notes become four chunks of two notes. Order 3, 2, 1, 0 plays those chunks backwards, so the line starts on B–C5 and ends on C–D. Inside each chunk the two notes keep their order. It is a rearrangement of the phrase, not a new scale.

Source: `packages/core/pattern.mjs`.

### bjork

**Call:** `.bjork(pulses)` or `.bjork("pulses:steps:rotation")`.

Euclidean rhythm written as one value. A colon list is read as pulses, steps, and an optional rotation. Steps default to the pulse count, and rotation defaults to 0.

```js
note("c4").s("triangle").bjork("3:8").decay(0.08).sustain(0).gain(0.2)
```

**Musical:** three attacks are spread across eight steps, the same grid as `euclid(3, 8)`. The gaps are as even as the numbers allow, so the hit pattern lopes instead of landing on every other step. `"5:8:1"` adds a one-step rotation, which moves where in the bar the pattern starts.

Source: `packages/core/euclid.mjs`.

### blshift

**Call:** `.blshift(bits)`.

Bitwise left shift: `a << b`. Each shift doubles the integer and drops the bits that fall off the left.

```js
n("0 1 2 3 4".blshift("<0 1>")).scale("C4:major").s("triangle").gain(0.2)
```

**Musical:** shift 0 leaves the degrees alone. Shift 1 doubles them, so 0, 1, 2, 3, 4 become 0, 2, 4, 6, 8. The contour stretches up the scale. It is not a transposition by a fixed interval; low degrees move a little and higher degrees move farther.

Source: `packages/core/pattern.mjs`.

### bmod

**Call:** `.bmod(config)`.

Modulates a control with audio from a `bus`. Set `b` or `bus` to the bus number. If `control` is omitted, the control written just before `bmod` is the one that moves. `depth` scales how far it moves.

```js
stack(
  note("c2*8").s("sawtooth").bus(1).dry(0).gain(0.15),
  note("c3 e3 g3 b3").s("sawtooth").lpf(900).bmod({ b: 1 }).gain(0.1)
)
```

**Musical:** the low sawtooth is silent on its own because `dry(0)` keeps it off the main output. Its shape still wiggles the filter of the upper arpeggio, so brightness pumps with the bass rhythm. The notes of the arpeggio do not change.

Source: `packages/core/controls.mjs`.

### bor

**Call:** `.bor(mask)`.

Bitwise OR: `a | b`. Bits that are set in the mask are forced on.

```js
n("0 1 2 3 4 5 6 7".bor(1)).scale("C4:major").s("triangle").gain(0.2)
```

**Musical:** OR with 1 forces every degree odd. Pairs collapse: 0 and 1 both become 1, 2 and 3 both become 3. The line still has eight attacks, but neighboring notes snap to the same pitch, a blunter melody.

Source: `packages/core/pattern.mjs`.

### bpattack

**Call:** `.bpattack(seconds)`. Alias: `bpa`.

Attack time of the band-pass filter envelope: how long the center frequency takes to move after the note starts. It does this only when `bpenv` gives the envelope some depth.

```js
note("c2 e2 f2 g2").s("sawtooth").bpf(500).bpattack("<.5 .25 .1 .01>").bpenv(4).gain(0.12)
```

**Musical:** a long attack makes the brightness swell in. A very short attack snaps the filter to its peak at the onset, a brighter pluck. The written notes stay the same. This is the filter's attack, not the loudness attack from `.attack`.

Source: `packages/core/controls.mjs`.

### bpdc

**Call:** `.bpdc(offset)`.

DC offset of the band-pass LFO. The source says to use 0 for a unipolar swing. With the LFO helpers, offset 0 starts the movement at the cutoff and adds the depth above it. A negative offset lets the cutoff move both below and above the written frequency.

```js
note("c3*8").s("sawtooth").bpf(800).bprate(2).bpdepth(400).bpdc("<0 -0.5>").gain(0.12)
```

**Musical:** the same wobble rate and depth either sit on top of 800 Hz or swing around it. One version only gets brighter than the written cutoff. The other dips duller as well. The pitch of the note does not change.

Source: `packages/core/controls.mjs`, `packages/superdough/helpers.mjs`.

### bpdecay

**Call:** `.bpdecay(seconds)`. Alias: `bpd`.

Decay time of the band-pass filter envelope. After the attack, the center frequency falls toward the sustain level of that envelope.

```js
note("c2 e2 f2 g2").s("sawtooth").bpf(500).bpdecay("<.5 .25 .1 0>").bpsustain(0.2).bpenv(4).gain(0.12)
```

**Musical:** a longer decay lets the brightness ring down. Decay 0 drops the filter as soon as the attack finishes. Sustain 0.2 is how high the filter settles, not how long the note lasts.

Source: `packages/core/controls.mjs`.

### bpdepth

**Call:** `.bpdepth(depth)`.

How far the band-pass LFO moves the cutoff, in the LFO's own depth units. `bprate` or `bpsync` sets how fast that movement repeats.

```js
note("c3*8").s("sawtooth").bpf(1000).bprate(4).bpdepth("<0 200 600>").gain(0.12)
```

**Musical:** depth 0 leaves the filter still. Larger depths make the tone pulse between dull and bright eight times per cycle, because the notes are steady and the filter is what moves. The pitch stays C3.

Source: `packages/core/controls.mjs`.

### bpdepthfrequency

**Call:** `.bpdepthfrequency(hertz)`. Alias: `bpdepthfreq`.

Depth of the band-pass LFO in hertz, so the number is a frequency swing you can hear as a bandwidth.

```js
note("c3 c3 c#3 c3 c3 c4").fast(2).s("sawtooth").bpf(800).bpdepthfrequency("<200 500 100 0>").gain(0.12)
```

**Musical:** 500 Hz of depth sweeps a wide bright band around the cutoff. 0 stops the sweep and the filter sits still. The melody is short and repeating so the filter motion is easy to separate from the pitch changes.

Source: `packages/core/controls.mjs`.

### bpenv

**Call:** `.bpenv(depth)`. Alias: `bpe`.

How far the band-pass envelope moves the center frequency. Positive depth opens the filter upward from `bpf`. Negative depth moves it the other way. The attack, decay, sustain, and release of this envelope are `bpattack`, `bpdecay`, `bpsustain`, and `bprelease`.

```js
note("c2 e2 f2 g2").s("sawtooth").bpf(500).bpattack(0.5).bpenv("<4 2 0 -2>").gain(0.12)
```

**Musical:** the same swell time covers a larger or smaller brightness change, and the negative value dulls the note instead of brightening it. Depth 0 leaves the filter on the written 500 Hz. This is timbre motion, not a change of pitch.

Source: `packages/core/controls.mjs`.

### bpf

**Call:** `.bpf(frequencyHz)`. Aliases: `bandf`, `bp`.

The documented name of the band-pass center frequency. A colon value can set frequency, Q, and envelope depth together: `.bpf("1000:3")`.

```js
note("c3 e3 g3 b3").s("sawtooth").bpf("<1000 2000 4000>").gain(0.12)
```

**Musical:** each cycle picks a higher slice of the sawtooth. The chord tones are the same; the vowel of the sound moves from round to thin. See `bandf` for the same control under the name stored on the event.

Source: `packages/core/controls.mjs`.

### bpq

**Call:** `.bpq(q)`. Alias: `bandq`.

The documented name of the band-pass resonance. The event stores it as `bandq`.

```js
note("c3*4").s("sawtooth").bpf(500).bpq("<0 1 2 3>").gain(0.12)
```

**Musical:** Q 0 is a wide, plain band. Q 3 rings closer to a whistle on the same C3. The rhythm does not change.

Source: `packages/core/controls.mjs`.

### bprate

**Call:** `.bprate(hertz)`.

Speed of the band-pass LFO in hertz. This is a clock in seconds, so it does not follow the cycle tempo. Pair it with `bpdepth` or `bpdepthfrequency`.

```js
note("c3*8").s("sawtooth").bpf(900).bprate("<1 4 8>").bpdepth(500).gain(0.12)
```

**Musical:** 1 Hz is a slow brightness swell. 8 Hz is a flutter. The eight notes stay on C3, so what you hear speeding up is the filter, not the melody.

Source: `packages/core/controls.mjs`.

### bprelease

**Call:** `.bprelease(seconds)`. Alias: `bpr`.

Release time of the band-pass filter envelope: how long the center frequency takes to settle after the note ends. `bpenv` has to be set for the movement to have somewhere to go.

```js
note("c2 e2 f2 g2").s("sawtooth").clip(0.5).bpf(500).bpenv(4).bprelease("<.5 .25 .1 0>").release(0.5).gain(0.12)
```

**Musical:** the loudness release is 0.5 seconds, so the tail is long enough to hear the filter move during it. A long filter release lets the brightness keep changing after the key-up. Release 0 snaps the filter shut with the note.

Source: `packages/core/controls.mjs`.

### bpshape

**Call:** `.bpshape(shape)`.

Waveform of the band-pass LFO. A number wraps through five shapes: 0 triangle, 1 sine, 2 ramp, 3 saw, 4 square. Names `tri`, `sine`, `ramp`, `saw`, and `square` select the same set.

```js
note("c3*8").s("sawtooth").bpf(900).bpsync(1).bpdepth(600).bpshape("<0 1 4>").gain(0.12)
```

**Musical:** triangle and sine glide the brightness. Square jumps between two brightnesses, a trill of timbre. The notes stay on C3 and the LFO still completes one wave per cycle because `bpsync(1)` is unchanged.

Source: `packages/core/controls.mjs`, `packages/superdough/helpers.mjs`.

### bpskew

**Call:** `.bpskew(skew)`.

Bends the band-pass LFO waveform. For the triangle and square shapes, the number is the point in the wave where it turns around. 0.5 is symmetrical.

```js
note("c3*8").s("sawtooth").bpf(900).bpsync(1).bpdepth(600).bpshape(0).bpskew("<0.2 0.5 0.8>").gain(0.12)
```

**Musical:** 0.2 puts the bright peak early in the cycle, a quick bloom and a long fall. 0.8 holds the rise and snaps down at the end. The pitch and the speed of the LFO stay put; the accent inside the sweep moves.

Source: `packages/core/controls.mjs`, `packages/superdough/worklets.mjs`.

### bpsustain

**Call:** `.bpsustain(level)`. Alias: `bps`.

Sustain level of the band-pass filter envelope. It is a level, not a time. After attack and decay, the cutoff holds here until release.

```js
note("c2 e2 f2 g2").s("sawtooth").bpf(500).bpdecay(0.5).bpsustain("<0 .25 .5 1>").bpenv(4).gain(0.12)
```

**Musical:** 0 lets the brightness fall away. 1 holds the filter at the top of the envelope, a steadily bright note. The pitches are the same four-note line.

Source: `packages/core/controls.mjs`.

### bpsync

**Call:** `.bpsync(cycles)`.

Speed of the band-pass LFO in cycles, so it locks to the tempo. 1 is one sweep per cycle. 4 is four sweeps per cycle.

```js
note("c3*8").s("sawtooth").bpf(900).bpsync("<1 2 4>").bpdepth(500).gain(0.12)
```

**Musical:** the brightness wave lines up with the bar. At 30 cycles per minute, `bpsync(1)` is a two-second sweep, and it stays a sweep-per-bar if you change `setcpm`. `bprate` would stay at a fixed number of hertz instead.

Source: `packages/core/controls.mjs`.

### brak

**Call:** `.brak()`.

On every other cycle, plays the pattern twice as fast, then silence, shifted a quarter cycle later. The other cycles play as written.

```js
note("c4 e4 g4 b4").s("triangle").brak().gain(0.2)
```

**Musical:** one cycle is a straight four-note line. The next compresses that line into half a cycle, lands it late by a quarter, and leaves a gap. The alternation is the lurch of a breakbeat. The pitches are the same; their placement in the bar changes.

Source: `packages/core/pattern.mjs`.

### brand

**Call:** `brand`, a pattern of 0 or 1.

Binary randomness with equal chance. It is `brandBy(0.5)`.

```js
note("c4*8").s("triangle").pan(brand).gain(0.2)
```

**Musical:** each note is thrown fully left (0) or fully right (1). The pitch and the eight attacks stay regular. What changes is where the note sits in the stereo field.

Source: `packages/core/signal.mjs`.

### brandBy

**Call:** `brandBy(probability)`.

Binary randomness where `probability` is the chance of 1. The rest of the time the value is 0.

```js
note("c4*8").s("triangle").pan(brandBy(0.2)).gain(0.2)
```

**Musical:** about two notes in ten go hard right, and the others stay hard left. The rhythm is still eight even attacks. Lower the probability and the right-hand notes become rarer accents in space.

Source: `packages/core/signal.mjs`.

### brshift

**Call:** `.brshift(bits)`.

Bitwise right shift: `a >> b`. Each shift halves the integer, dropping the low bit.

```js
n("0 1 2 3 4 5 6 7".brshift("<0 1>")).scale("C4:major").s("triangle").gain(0.2)
```

**Musical:** shift 0 is the scale run. Shift 1 folds it downward: 0 and 1 become 0, 2 and 3 become 1, 4 and 5 become 2. Pairs of degrees share a pitch, and the line sits lower. It is a fold of the contour, not a transposition down by one scale step.

Source: `packages/core/pattern.mjs`.

### bus

**Call:** `.bus(number)`.

Sends the pattern to a numbered mix bus. Another pattern can play that bus or modulate from it with `bmod`. The send still follows the pattern's own gain unless `dry` turns down the direct output.

```js
stack(
  note("c2*4").s("sawtooth").bus(1).dry(0).gain(0.15),
  s("bus").n(1).gain(0.5)
)
```

**Musical:** the low pulse is sent to bus 1 and kept off the main output. `s("bus").n(1)` is the return, so you hear that pulse through the bus. Effects chained on the return sit on the copy. Several parts can share one processing path by sending to the same number.

Source: `packages/core/controls.mjs`.

### busgain

**Call:** `.busgain(amount)`. Alias: `bgain`.

Gain applied to the signal as it is sent to the bus, before other patterns hear it.

```js
stack(
  note("c2*4").s("sawtooth").bus(1).busgain("<0.2 1>").dry(0).gain(0.2),
  s("bus").n(1).gain(0.5)
)
```

**Musical:** the direct sound is off, and the return on bus 1 is what you hear. The send alternates between a quiet copy and a full one. The written notes stay the same; only how hard they hit the bus changes.

Source: `packages/core/controls.mjs`.

### bxor

**Call:** `.bxor(mask)`.

Bitwise exclusive or: `a ^ b`. Bits that differ between the value and the mask are set.

```js
n("0 1 2 3 4 5 6 7".bxor(1)).scale("C4:major").s("triangle").gain(0.2)
```

**Musical:** XOR with 1 flips the lowest bit. 0 swaps with 1, 2 swaps with 3, and so on. Each pair of scale degrees trades places, a small neighbor inversion. The eight attacks stay in time.

Source: `packages/core/pattern.mjs`.

### bypass

**Call:** `.bypass(flag)`.

Silences the pattern when the flag is a non-zero integer. Zero lets the pattern through.

```js
note("c4 e4 g4 b4").s("triangle").bypass("<0 1>").gain(0.2)
```

**Musical:** alternate cycles are muted. The phrase is still four notes when it plays; the missing cycles are the gap. It is a mute switch, not a filter.

Source: `packages/core/pattern.mjs`.

### byteBeatExpression

**Call:** `.byteBeatExpression(expression)` with `s("bytebeat")`. Aliases: `bbexpr`, `bb`.

The bitwise formula used as a bytebeat waveform. The variable in the formula is the running sample time.

```js
s("bytebeat").byteBeatExpression("t*(t>>15^t>>66)").gain(0.15)
```

**Musical:** the tone is the formula heard as audio. Shifts and multiplies fold the time counter into a harsh digital melody, with pitch jumps that come from the bit math. A different expression is a different piece. Note names are not what set the pitch here.

Source: `packages/core/controls.mjs`.

### byteBeatStartTime

**Call:** `.byteBeatStartTime(samples)`. Alias: `bbst`.

Starting value of the bytebeat time counter, in samples. The same formula begins later in its sequence.

```js
note("c3*8".add("{0 0 12 0 7 5 3}%8")).s("bytebeat:5").byteBeatStartTime("<0 30000>").gain(0.15)
```

**Musical:** both cycles use the same bytebeat preset and the same pitch pattern. The later start time opens the formula in a different place, so the timbre and the internal rhythm of the digital tone change while the note grid stays put.

Source: `packages/core/controls.mjs`.
