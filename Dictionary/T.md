### T

- `tables`
- `tag`
- `timeCat` — alias of `stepcat`
- `timecat` — alias of `stepcat`
- `timeline`
- `toBipolar`
- `trans`
- `transient`
- `transpose`
- `transsustain`
- `trem` — alias of `tremolo`
- `tremdepth` — alias of `tremolodepth`
- `tremolo`
- `tremolodepth`
- `tremolophase`
- `tremoloshape`
- `tremoloskew`
- `tremolosync`
- `tremphase` — alias of `tremolophase`
- `tremshape` — alias of `tremoloshape`
- `tremskew` — alias of `tremoloskew`
- `tremsync` — alias of `tremolosync`
- `triode`
- `tscope` — alias of `scope`
- `tsdelay`
- `tune`
- `tuning`

## Entries

### tables

**Call:** `tables`.

Loads a collection of wavetables to use with `s`

Source: `packages/superdough/wavetable.mjs`.

### tag

**Call:** `.tag(tag)`.

Tags each Hap with an identifier. Good for filtering. The function populates Hap.context.tags (Array).

```js
s("saw!16").note("F1")
  .lpf(tri.range(40, 80).slow(4)).lpenv(5).lpq(4).lpd(0.15)
  .when(rand.late(0.1).gte(0.5), x => x.transpose("12").tag('altered'))
  .when(rand.late(0.2).gte(0.5), x => x.s("square").tag('altered'))
  .when("<0 1>", x => x.filter((hap) => hap.hasTag('altered')))
```

Source: `packages/core/pattern.mjs`.

### timeline

**Call:** `.timeline()`.

Allows you to switch a pattern between different 'timelines'. This is particularly useful when
live coding, for example when you want to cue a pattern up to play from its start.

Timelines are specified by number, so that if you had a pattern like
`n("<0 1 2 3>").s("num").timeline(1)` playing, then changed the '1'
to '2', it would always align '0' to the nearest cycle. You will likely want to trigger
an evaluation a little bit before the cycle starts, to avoid missing events.

After the first use, a timeline will continue with the same 'offset'. That is, if you change
a pattern without changing its timeline number, it will stay on that timeline without resetting.

Rather than incrementing a timeline to reset it, it's easier to negate it, e.g. by switching between `-2`
and `2`. This is because when you negate a timeline it will always reset.

You can also pattern the timeline if you want, to create strange resetting patterns.


n("<0 1 2 3>(3,8)")
  .sound("num")
  // resets the timeline every two cycles, by negating the timeline.
  // in a lot of cases this will be edited by a human live coder
  // rather than patterned!
  .timeline("<2 -2>".slow(2))

Source: `packages/core/impure.mjs`.

### toBipolar

**Call:** `.toBipolar()`.

Assumes a numerical pattern, containing unipolar values in the range 0 ..
1. Returns a new pattern with values scaled to the bipolar range -1 .. 1

Source: `packages/core/pattern.mjs`.

### trans

**Call:** `.trans(amount)`. Same as `transpose`.

Change the pitch of each value by the given amount. Expects numbers or note strings as values.
The amount can be given as a number of semitones or as a string in interval short notation.
If you don't care about enharmonic correctness, just use numbers. Otherwise, pass the interval of
the form: ST where S is the degree number and T the type of interval with

- M = major
- m = minor
- P = perfect
- A = augmented
- d = diminished

Examples intervals:

- 1P = unison
- 3M = major third
- 3m = minor third
- 4P = perfect fourth
- 4A = augmented fourth
- 5P = perfect fifth
- 5d = diminished fifth

```js
"c2 c3".fast(2).transpose("<0 -2 5 3>".slow(2)).note()
```

```js
"c2 c3".fast(2).transpose("<1P -2M 4P 3m>".slow(2)).note()
```

Source: `packages/tonal/tonal.mjs`.

### transient

**Call:** `.transient(attack, sustain)`.

Transient shaper. Gives independent control over the emphasis on transients
and sustains

```js
s("bd").transient("<-1 -0.5 0 0.5 1>")
```

```js
s("hh*16").bank("tr909").transient("<-1:1 1:-1>")
```

Source: `packages/core/controls.mjs`.

### transpose

**Call:** `.transpose(amount)`. Alias: `trans`.

Change the pitch of each value by the given amount. Expects numbers or note strings as values.
The amount can be given as a number of semitones or as a string in interval short notation.
If you don't care about enharmonic correctness, just use numbers. Otherwise, pass the interval of
the form: ST where S is the degree number and T the type of interval with

- M = major
- m = minor
- P = perfect
- A = augmented
- d = diminished

Examples intervals:

- 1P = unison
- 3M = major third
- 3m = minor third
- 4P = perfect fourth
- 4A = augmented fourth
- 5P = perfect fifth
- 5d = diminished fifth

```js
"c2 c3".fast(2).transpose("<0 -2 5 3>".slow(2)).note()
```

```js
"c2 c3".fast(2).transpose("<1P -2M 4P 3m>".slow(2)).note()
```

Source: `packages/tonal/tonal.mjs`.

### transsustain

**Call:** `.transsustain(level)`.

Sustain emphasis of the transient shaper. `transient` is the attack emphasis, from -1 to 1, and this is the sustain emphasis on the same scale. A colon value to `transient` can set both, because they are registered together.

```js
s("hh*8").bank("RolandTR909").transient(0.4).transsustain("<-1 0 1>")
```

Source: `packages/core/controls.mjs`.

### tremolo

**Call:** `.tremolo(speed)`. Alias: `trem`.

Modulate the amplitude of a sound with a continuous waveform

```js
note("d d d# d".fast(4)).s("supersaw").tremolo("<3 2 100> ").tremoloskew("<.5>")
```

Source: `packages/core/controls.mjs`.

### tremolodepth

**Call:** `.tremolodepth(depth)`. Alias: `tremdepth`.

Depth of amplitude modulation

```js
note("a1 a1 a#1 a1".fast(4)).s("pulse").tremsync(4).tremolodepth("<1 2 .7>")
```

Source: `packages/core/controls.mjs`.

### tremolophase

**Call:** `.tremolophase(offset)`. Alias: `tremphase`.

Alter the phase of the modulation waveform

```js
note("{f a c e}%16").s("sawtooth").tremsync(4).tremolophase("<0 .25 .66>")
```

Source: `packages/core/controls.mjs`.

### tremoloshape

**Call:** `.tremoloshape(shape)`. Alias: `tremshape`.

Shape of amplitude modulation

```js
note("{f g c d}%16").tremsync(4).tremoloshape("<sine tri square>").s("sawtooth")
```

Source: `packages/core/controls.mjs`.

### tremoloskew

**Call:** `.tremoloskew(amount)`. Alias: `tremskew`.

Alter the shape of the modulation waveform

```js
note("{f a c e}%16").s("sawtooth").tremsync(4).tremoloskew("<.5 0 1>")
```

Source: `packages/core/controls.mjs`.

### tremolosync

**Call:** `.tremolosync(cycles)`. Alias: `tremsync`.

Modulate the amplitude of a sound with a continuous waveform

```js
note("d d d# d".fast(4)).s("supersaw").tremolosync("4").tremoloskew("<1 .5 0>")
```

Source: `packages/core/controls.mjs`.

### triode

**Call:** `.triode(amount)`.

Triode distortion. The browser synth does not read this control. It is registered with the other SuperDirt effects, next to `waveloss`.

```js
note("c3").s("sawtooth").triode("<0 .4 .8>").osc().gain(0.15)
```

Source: `packages/core/controls.mjs`.

### tsdelay

**Call:** `.tsdelay(time)`.

A delay registered with `xsdelay`. The browser synth does not read this control. It is registered with the other SuperDirt effects, next to `waveloss`.

```js
note("c3 ~").s("sawtooth").tsdelay("<0 .2 .5>").osc().gain(0.15)
```

Source: `packages/core/controls.mjs`.

### tune

**Call:** `.tune(scale)`.

Deprecated.

Assumes pattern contains numerical scale degrees on the `i` control (see examples below). Accepts a scale name or list of frequencies (see all available names at the link on the reference). Returns a new pattern with all values mapped to a frequency ratio. Similar to `xen`.

```js
i("0 1 2 3 4 5").tune("hexany15").mul("220").freq()
```

```js
// You can set your root to be a
// particular note with getFreq:
i("4 8 9 10 - - 5 7 9 11 - -").tune("tranh3")
  .mul(getFreq('c3'))
  .freq().clip(.5).room(1)
```

```js
// You can also give tune a list of
// frequencies to use as the scale:
i("0 1 2 3 4").tune([
  261.6255653006,
  302.72962012827,
  350.29154279212,
  405.32593044476,
  469.00678383895,
  523.2511306012
]).mul(220).freq();
```

Source: `packages/xen/tune.mjs`.

### tuning

**Call:** `.tuning(ratios)`.

Maps a numeric pattern through a list of frequency ratios. The index wraps, and each extra trip around the list multiplies the ratio by 2, so the list repeats at the octave. The source calls this an early version of `xen`. The result is a ratio, so multiply by a root frequency before `freq`.

```js
n("0 1 2 3").tuning([1, 1.25, 1.5, 2]).mul(220).freq().s("triangle").gain(0.2)
```

Source: `packages/xen/xen.mjs`.
