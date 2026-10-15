### D

- `datt` — alias of `duckattack`
- `dec` — alias of `decay`
- `decay`
- `degrade`
- `degradeBy`
- `degradeByWith`
- `degree`
- `delay`
- `delayfb` — alias of `delayfeedback`
- `delayfeedback`
- `delays` — alias of `delaysync`
- `delayspeed`
- `delaysync`
- `delayt` — alias of `delayspeed`
- `delaytime`
- `deltaSlide`
- `density`
- `det` — alias of `detune`
- `detune`
- `dfb` — alias of `delayfeedback`
- `dictionary`
- `diode`
- `dist` — alias of `distort`
- `distort`
- `distortion` — alias of `distortvol`
- `distorttype`
- `distortvol`
- `disttype` — alias of `distorttype`
- `distvol` — alias of `distortvol`
- `div`
- `djf`
- `dough`
- `drive`
- `dry`
- `ds`
- `dt` — alias of `delayspeed`
- `duck` — alias of `duckorbit`
- `duckatt` — alias of `duckattack`
- `duckattack`
- `duckdepth`
- `duckons` — alias of `duckonset`
- `duckonset`
- `duckorbit`
- `dur` — alias of `duration`
- `duration`

## Entries

### decay

**Call:** `.decay(time)`. Alias: `dec`.

Amplitude envelope decay time: the time it takes after the attack time to reach the sustain level.
Note that the decay is only audible if the sustain value is lower than 1.

```js
note("c3 e3 f3 g3").decay("<.1 .2 .3 .4>").sustain(0)
```

Source: `packages/core/controls.mjs`.

### degrade

**Call:** `.degrade()`.

Randomly removes 50% of events from the pattern. Shorthand for `.degradeBy(0.5)`

```js
s("hh*8").degrade()
```

```js
s("[hh?]*8")
```

Source: `packages/core/signal.mjs`.

### degradeBy

**Call:** `.degradeBy(amount)`.

Randomly removes events from the pattern by a given amount.
0 = 0% chance of removal
1 = 100% chance of removal

```js
s("hh*8").degradeBy(0.2)
```

```js
s("[hh?0.2]*8")
```

```js
//beat generator
s("bd").segment(16).degradeBy(.5).ribbon(16,1)
```

Source: `packages/core/signal.mjs`.

### degradeByWith

**Call:** `.degradeByWith(test, testAgainst)`.

`degradeByWith` is like `degradeBy`, but with control over the random or other signal used to filter out the events.

`degradeBy(x)` is essentially `degradeByWith(rand, x)`

This allows you to do things other than with `rand`, see examples below

```js
note("c a f e").degradeByWith(sine, .1)
```

```js
note("c a f e").degradeByWith(perlin, .5)
```

```js
note("c a f e").degradeByWith(sine, cosine)
```

Source: `packages/core/signal.mjs`.

### degree

**Call:** `.degree(amount)`.

Registered control. The source says it was not found in the Tidal documentation, and this checkout does not apply it.

```js
n("0 2 4").scale("C:major").degree(1).s("triangle").gain(0.2)
```

Source: `packages/core/controls.mjs`.

### delay

**Call:** `.delay(level)`.

Sets the level of the delay signal.

When using mininotation, you can also optionally add the 'delaytime' and 'delayfeedback' parameter,
separated by ':'.

```js
s("bd bd").delay("<0 .25 .5 1>")
```

```js
s("bd bd").delay("0.65:0.25:0.9 0.65:0.125:0.7")
```

Source: `packages/core/controls.mjs`.

### delayfeedback

**Call:** `.delayfeedback(feedback)`. Aliases: `delayfb`, `dfb`.

Sets the level of the signal that is fed back into the delay.
Caution: Values >= 1 will result in a signal that gets louder and louder! Don't do it

```js
s("bd").delay(.25).delayfeedback("<.25 .5 .75 1>")
```

Source: `packages/core/controls.mjs`.

### delayspeed

**Call:** `.delayspeed(delayspeed)`. Aliases: `delayt`, `dt`.

Sets the time of the delay effect.

```js
note("d d a# a".fast(2)).s("sawtooth").delay(.8).delaytime(1/2).delayspeed("<2 .5 -1 -2>")
```

Source: `packages/core/controls.mjs`.

### delaysync

**Call:** `.delaysync(cycles)`. Aliases: `delays`, `ds`.

Sets the time of the delay effect in cycles.

```js
s("bd bd").delay(.25).delaysync("<1 2 3 5>".div(8))
```

Source: `packages/core/controls.mjs`.

### delaytime

**Call:** `.delaytime(delay)`. Aliases: `delayt`, `dt`.

Sets the time of the delay effect in seconds.

```js
note("d d a# a".fast(2))
.s("sawtooth")
.delay(.8)
.delaytime(1/2)
.delayspeed("<2 .5 -1 -2>")
```

Source: `packages/core/controls.mjs`.

### deltaSlide

**Call:** `.deltaSlide(amount)`.

Pitch acceleration of a ZZFX sound. `slide` is the pitch glide, and this value changes that glide while the sound plays.

```js
s("z_sine").note("c3").slide(0.2).deltaSlide("<0 1 3>").gain(0.2)
```

Source: `packages/core/controls.mjs`.

### density

**Call:** `.density(density)`. Same as `fast`.

Speed up a pattern by the given factor. Used by "*" in mini notation.

```js
s("crackle*4").density("<0.01 0.04 0.2 0.5>".slow(4))
```

Source: `packages/core/controls.mjs`.

### detune

**Call:** `.detune(amount)`. Alias: `det`.

Set detune for stacked voices of supported oscillators.

```js
note("d f a a# a d3").fast(2).s("supersaw").detune("<.1 .2 .5 24.1>")
```

Source: `packages/core/controls.mjs`.

### dictionary

**Call:** `.dictionary(dictionaryName)`.

Which dictionary to use for the voicings. This falls back to the default dictionary if not provided

```js
addVoicings('house', {
'': ['7 12 16', '0 7 16', '4 7 12'],
'm': ['0 3 7']
})
chord("<Am C D F Am E Am E>")
.dict('house').anchor(66)
.voicing().room(.5)
```

Source: `packages/core/controls.mjs`.

### diode

**Call:** `.diode(distortion, volume)`.

Diode-emulating distortion

Source: `packages/core/pattern.mjs`.

### distort

**Call:** `.distort(distortion, volume, type)`. Alias: `dist`.

Wave shaping distortion. CAUTION: it can get loud.
Second option in optional array syntax (ex: ".9:.5") applies a postgain to the output. Third option sets the waveshaping type.
Most useful values are usually between 0 and 10 (depending on source gain). If you are feeling adventurous, you can turn it up to 11 and beyond ;)

```js
s("bd sd [~ bd] sd,hh*8").distort("<0 2 3 10:.5>")
```

```js
note("d1!8").s("sine").penv(36).pdecay(.12).decay(.23).distort("8:.4")
```

```js
s("bd:4*4").bank("tr808").distort("3:0.5:diode")
```

Source: `packages/core/controls.mjs`.

### distorttype

**Call:** `.distorttype(type)`. Alias: `disttype`.

Type of waveshaping distortion to apply.

```js
s("bd*4").bank("tr909").distort(2).distorttype("<0 1 2>")
```

```js
s("sine").note("F1*2").release(1)
  .penv(24).pdecay(0.05)
  .distort(rand.range(1, 8))
  .distorttype("<fold chebyshev scurve diode asym sinefold>")
```

Source: `packages/core/controls.mjs`.

### distortvol

**Call:** `.distortvol(volume)`. Aliases: `distortion`, `distvol`.

Postgain for waveshaping distortion.

```js
s("bd*4").bank("tr909").distort(2).distortvol(0.8)
```

Source: `packages/core/controls.mjs`.

### div

**Call:** `div`.

Divides each number by the given factor.

Source: `packages/core/pattern.mjs`.

### djf

**Call:** `.djf(cutoff)`.

DJ filter, below 0.5 is low pass filter, above is high pass filter.

```js
n(irand(16).seg(8)).scale("d:phrygian").s("supersaw").djf("<.5 .3 .2 .75>")
```

Source: `packages/core/controls.mjs`.

### dough

**Call:** `.dough()`.

Uses dough as the audio engine. more info at https://dough.strudel.cc

```js
$: chord("<Dm9 Dm11 Dm7>").offset("<-1 0 1 0>").voicing()
.phaser(3).fm(1.4).fmh(1.01)
.dough()
```

Source: `packages/dough/dough.mjs`.

### drive

**Call:** `.drive(amount)`.

Filter overdrive for supported filter types

```js
note("{f g g c d a a#}%16".sub(17)).s("supersaw").lpenv(8).lpf(150).lpq(.8).ftype('ladder').drive("<.5 4>")
```

Source: `packages/core/controls.mjs`.

### dry

**Call:** `.dry(dry)`.

Set dryness of reverb. See `room` and `size` for more information about reverb.

```js
n("[0,3,7](3,8)").s("superpiano").room(.7).dry("<0 .5 .75 1>").osc()
```

Source: `packages/core/controls.mjs`.

### ds

**Call:** `.ds(cycles)`. Same as `delaysync`.

Sets the time of the delay effect in cycles.

```js
s("bd bd").delay(.25).delaysync("<1 2 3 5>".div(8))
```

Source: `packages/core/controls.mjs`.

### duckattack

**Call:** `.duckattack(time)`. Aliases: `duckatt`, `datt`.

The time required for the ducked signal(s) to return to their normal volume.

Can vary across orbits with the ':' mininotation, e.g. `duckonset("0:0.003")`.
Note: this requires first applying the effect to multiple orbits with e.g. `duckorbit("2:3")`.

```js
sound: n(run(8)).scale("c:minor").s("sawtooth").delay(.7).orbit(2)
ducker: s("bd:4!4").beat("0,4,8,11,14",16).duckorbit(2).duckattack("<0.2 0 0.4>").duckdepth(1)
```

```js
moreduck: n(run(8)).scale("c:minor").s("sawtooth").delay(.7).orbit(2)
lessduck: s("hh*16").orbit(5)
ducker: s("bd:4!4").beat("0,4,8,11,14",16).duckorbit("2:5").duckattack("0.4:0.1")
```

Source: `packages/core/controls.mjs`.

### duckdepth

**Call:** `.duckdepth(depth)`.

The amount of ducking applied to target orbit

Can vary across orbits with the ':' mininotation, e.g. `duckdepth("0.3:0.1")`.
Note: this requires first applying the effect to multiple orbits with e.g. `duckorbit("2:3")`.

```js
stack( n(run(8)).scale("c:minor").s("sawtooth").delay(.7).orbit(2), s("bd:4!4").beat("0,4,8,11,14",16).duckorbit(2).duckattack(0.2).duckdepth("<1 .9 .6 0>"))
```

```js
$: n(run(16)).scale("c:minor:pentatonic").s("sawtooth").delay(.7).orbit(2)
$: s("hh*16").orbit(3)
$: s("bd:4!4").beat("0,4,8,11,14",16).duckorbit("2:3").duckattack(0.2).duckdepth("1:0.5")
```

Source: `packages/core/controls.mjs`.

### duckonset

**Call:** `.duckonset(time)`. Alias: `duckons`.

The time required for the ducked signal(s) to reach their lowest volume.
Can be used to prevent clicking or for creative rhythmic effects.

Can vary across orbits with the ':' mininotation, e.g. `duckonset("0:0.003")`.
Note: this requires first applying the effect to multiple orbits with e.g. `duckorbit("2:3")`.

```js
// Clicks
sound: freq("63.2388").s("sine").orbit(2).gain(4)
duckerWithClick: s("bd*4").duckorbit(2).duckattack(0.3).duckonset(0).postgain(0)
```

```js
// No clicks
sound: freq("63.2388").s("sine").orbit(2).gain(4)
duckerWithoutClick: s("bd*4").duckorbit(2).duckattack(0.3).duckonset(0.01).postgain(0)
```

```js
// Rhythmic
noise: s("pink").distort("2:1").orbit(4) // used rhythmically with 0.3 onset below
hhat: s("hh*16").orbit(7)
ducker: s("bd*4").bank("tr909").duckorbit("4:7").duckonset("0.3:0.003").duckattack(0.25)
```

Source: `packages/core/controls.mjs`.

### duckorbit

**Call:** `.duckorbit(orbit)`. Alias: `duck`.

Modulate the amplitude of an orbit to create a "sidechain" like effect.

Can be applied to multiple orbits with the ':' mininotation, e.g. `duckorbit("2:3")`

```js
$: n(run(16)).scale("c:minor:pentatonic").s("sawtooth").delay(.7).orbit(2)
$: s("bd:4!4").beat("0,4,8,11,14",16).duckorbit(2).duckattack(0.2).duckdepth(1)
```

```js
$: n(run(16)).scale("c:minor:pentatonic").s("sawtooth").delay(.7).orbit(2)
$: s("hh*16").orbit(3)
$: s("bd:4!4").beat("0,4,8,11,14",16).duckorbit("2:3").duckattack(0.2).duckdepth(1)
```

Source: `packages/core/controls.mjs`.

### duration

**Call:** `.duration(seconds)`. Alias: `dur`.

Sets the duration of the event in cycles. Similar to clip / legato, it also cuts samples off at the end if they exceed the duration.

```js
note("c a f e").s("piano").dur("<.5 1 2>")
```

Source: `packages/core/controls.mjs`.
