### G

- `gain`
- `gap`
- `gate`
- `getClockTime`
- `getCps`
- `getDuration`
- `getFreq` — alias of `getFrequency`
- `getFrequency`
- `getTime`
- `glide`
- `gravityX`
- `gravityY`
- `gravityZ`
- `gravX` — alias of `gravityX`
- `gravY` — alias of `gravityY`
- `gravZ` — alias of `gravityZ`
- `group`
- `groupmod`
- `grow`
- `gt`
- `gte`

## Entries

### gain

**Call:** `.gain(amount)`.

Controls the gain by an exponential amount.

```js
s("hh*8").gain(".4!2 1 .4!2 1 .4 1").fast(2)
```

Source: `packages/core/controls.mjs`.

### gap

**Call:** `gap(steps)`.

Does absolutely nothing, but with a given metrical 'steps'

```js
gap(3) // "~@3"
```

Source: `packages/core/pattern.mjs`.

### gate

**Call:** `.gate(level)`.

Gate control, with alias `gat`. The source points at Tidal's control-voltage gate. The browser synth does not read it.

```js
note("c4*4").s("triangle").gate("<1 0>").gain(0.2)
```

Source: `packages/core/controls.mjs`.

### getClockTime

**Call:** `getClockTime()`.

Returns the scheduler's current clock time in seconds, the same clock `onSchedule` uses. It throws if playback has not set a clock.

```js
getClockTime()
```

Source: `packages/core/schedulerState.mjs`.

### getCps

**Call:** `getCps()`.

Returns the scheduler's current cycles per second. `setcps` and `setcpm` are what change it.

```js
getCps()
```

Source: `packages/core/schedulerState.mjs`.

### getDuration

**Call:** `getDuration(sampleName)`.

Returns the duration, in seconds, of the given sample.
Has optional param `n` (for instance, the `2` in `s("casio:2")`)

Note: `must` be called with await, otherwise you'll get a pending Promise object.

```js
// Set a patterns cycle length to exactly the length of the sample
samples('github:tidalcycles/dirt-samples')
let k = await getDuration('sax')
s("sax").cps(1/k)
```

Source: `packages/superdough/sampler.mjs`.

### getFrequency

**Call:** `getFrequency(input)`. Alias: `getFreq`.

Given a hap, returns the frequency of the note or freq, if defined

Given a note, returns the frequency of that note
`getFreq('c3')`

Given a midi note number, returns the frequency of that midi note
`getFreq('c3')`

```js
i("4 8 9 10 - - 5 7 9 11 - -").tune("tranh3")
.mul(getFreq('c3'))
.freq().clip(.5).room(1)
```

Source: `packages/core/util.mjs`.

### getTime

**Call:** `getTime()`.

Returns the scheduler's current time in cycles. It throws if playback has not set a time source.

```js
getTime()
```

Source: `packages/core/schedulerState.mjs`.

### glide

**Call:** `.glide(amount)`.

Dough control registered beside `group` and `voices`. The source does not define the glide time, and the browser synth does not read it.

```js
note("c3 e3 g3").s("sawtooth").glide(0.1).gain(0.15)
```

Source: `packages/dough/lib.mjs`.

### gravityX

**Call:** `gravityX`. Alias: `gravX`.

The device's gravity x-axis value ranges from 0 to 1.

```js
n(gravityX.segment(4).range(0,7)).scale("C:minor")
```

Source: `packages/motion/motion.mjs`.

### gravityY

**Call:** `gravityY`. Alias: `gravY`.

The device's gravity y-axis value ranges from 0 to 1.

```js
n(gravityY.segment(4).range(0,7)).scale("C:minor")
```

Source: `packages/motion/motion.mjs`.

### gravityZ

**Call:** `gravityZ`. Alias: `gravZ`.

The device's gravity z-axis value ranges from 0 to 1.

```js
n(gravityZ.segment(4).range(0,7)).scale("C:minor")
```

Source: `packages/motion/motion.mjs`.

### group

**Call:** `.group(id)`.

Group id used by dough. `groupmod` copies this id onto a modulator so dough can update that group.

```js
note("c3 e3 g3").s("sawtooth").group(1).gain(0.15)
```

Source: `packages/dough/lib.mjs`.

### groupmod

**Call:** `.groupmod(modulator)`.

Stacks the pattern with a dough update. The modulator events keep the pattern's `group` id and are marked `dough: 'update_group'`. `gmod` is the same method. This is for the dough backend.

```js
note("c3").s("sawtooth").group(1).groupmod(note("g3").gain(0.1))
```

Source: `packages/dough/lib.mjs`.

### grow

**Call:** `.grow()`.

*Experimental*

Progressively grows the pattern by 'n' steps until the full pattern is played, or if a second value is given (using mininotation list syntax with `:`),
that number of times.
A positive number will progressively grow steps from the start of a pattern, and a negative number from the end.



"tha dhi thom nam".grow("1").sound()
.bank("mridangam")

"tha dhi thom nam".grow("-1").sound()
.bank("mridangam")

"tha dhi thom nam".grow("1 -1").sound().bank("mridangam").pace(4)

note("0 1 2 3 4 5 6 7".scale("C:ritusen")).sound("folkharp")
.grow("1 -1").pace(8)

Source: `packages/core/pattern.mjs`.

### gt

**Call:** `gt(a, b)`.

performs a > b

Source: `packages/core/pattern.mjs`.

### gte

**Call:** `gte(a, b)`.

performs a >= b

Source: `packages/core/pattern.mjs`.
