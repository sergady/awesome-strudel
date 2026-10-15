### H

- `hard`
- `harmonic`
- `hbrick`
- `hcutoff`
- `hold`
- `hours`
- `hp` — alias of `hpf`
- `hpa` — alias of `hpattack`
- `hpattack`
- `hpd` — alias of `hpdecay`
- `hpdc`
- `hpdecay`
- `hpdepth`
- `hpdepthfreq` — alias of `hpdepthfrequency`
- `hpdepthfrequency`
- `hpe` — alias of `hpenv`
- `hpenv`
- `hpf`
- `hpq`
- `hpr` — alias of `hprelease`
- `hprate`
- `hprelease`
- `hps` — alias of `hpsustain`
- `hpshape`
- `hpskew`
- `hpsustain`
- `hpsync`
- `hresonance`
- `hsl`
- `hsla`
- `hurry`

## Entries

### hard

**Call:** `.hard(distortion, volume)`.

Hard-clipping distortion

Source: `packages/core/pattern.mjs`.

### harmonic

**Call:** `.harmonic(amount)`.

Registered control. The source says it was not found in the Tidal documentation, and this checkout does not apply it.

```js
note("c4").s("triangle").harmonic(2).gain(0.2)
```

Source: `packages/core/controls.mjs`.

### hbrick

**Call:** `.hbrick(frequency)`.

High brickwall cutoff. The browser synth does not read this control. It is registered with the other SuperDirt effects, next to `waveloss`.

```js
note("c3").s("sawtooth").hbrick("<2000 8000>").osc().gain(0.15)
```

Source: `packages/core/controls.mjs`.

### hcutoff

**Call:** `.hcutoff(frequency)`. Same as `hpf`.

Applies the cutoff frequency of the **h**igh-**p**ass **f**ilter.

When using mininotation, you can also optionally add the 'hpq' parameter, separated by ':'.

```js
s("bd sd [~ bd] sd,hh*8").hpf("<4000 2000 1000 500 200 100>")
```

```js
s("bd sd [~ bd] sd,hh*8").hpf("<2000 2000:25>")
```

Source: `packages/core/controls.mjs`.

### hold

**Call:** `.hold(time)`.

Registered beside `release`, with no further comment. The browser envelope uses `attack`, `decay`, `sustain`, and `release`, and does not read `hold`.

```js
note("c4 e4 g4").s("triangle").hold(0.2).gain(0.2)
```

Source: `packages/core/controls.mjs`.

### hours

**Call:** `.hours(count)`.

Registered with `minutes`, `seconds`, and `songPtr` as clock metadata. This checkout does not apply it.

```js
note("c4").s("triangle").hours(0).gain(0.2)
```

Source: `packages/core/controls.mjs`.

### hpattack

**Call:** `.hpattack(attack)`. Alias: `hpa`.

Sets the attack duration for the highpass filter envelope.

```js
note("c2 e2 f2 g2")
.sound('sawtooth')
.hpf(500)
.hpa("<.5 .25 .1 .01>/4")
.hpenv(4)
```

Source: `packages/core/controls.mjs`.

### hpdc

**Call:** `.hpdc(dcoffset)`.

DC offset of the LFO for the highpass filter

Source: `packages/core/controls.mjs`.

### hpdecay

**Call:** `.hpdecay(decay)`. Alias: `hpd`.

Sets the decay duration for the highpass filter envelope.

```js
note("c2 e2 f2 g2")
.sound('sawtooth')
.hpf(500)
.hpd("<.5 .25 .1 0>/4")
.hps(0.2)
.hpenv(4)
```

Source: `packages/core/controls.mjs`.

### hpdepth

**Call:** `.hpdepth(depth)`.

Depth of the LFO for the highpass filter

Source: `packages/core/controls.mjs`.

### hpdepthfrequency

**Call:** `.hpdepthfrequency(depth)`. Alias: `hpdepthfreq`.

Depth of the LFO for the hipass filter, in hz

```js
note("<c c c# c c c4>*16").s("sawtooth").lpf(600).hpdepthfrequency("<200 500 100 0>")
```

Source: `packages/core/controls.mjs`.

### hpenv

**Call:** `.hpenv(modulation)`. Alias: `hpe`.

Sets the highpass filter envelope modulation depth.

```js
note("c2 e2 f2 g2")
.sound('sawtooth')
.hpf(500)
.hpa(.5)
.hpenv("<4 2 1 0 -1 -2 -4>/4")
```

Source: `packages/core/controls.mjs`.

### hpf

**Call:** `.hpf(frequency)`. Aliases: `hp`, `hcutoff`.

Applies the cutoff frequency of the **h**igh-**p**ass **f**ilter.

When using mininotation, you can also optionally add the 'hpq' parameter, separated by ':'.

```js
s("bd sd [~ bd] sd,hh*8").hpf("<4000 2000 1000 500 200 100>")
```

```js
s("bd sd [~ bd] sd,hh*8").hpf("<2000 2000:25>")
```

Source: `packages/core/controls.mjs`.

### hpq

**Call:** `.hpq(q)`. Alias: `hresonance`.

Controls the **h**igh-**p**ass **q**-value.

```js
s("bd sd [~ bd] sd,hh*8").hpf(2000).hpq("<0 10 20 30>")
```

Source: `packages/core/controls.mjs`.

### hprate

**Call:** `.hprate(rate)`.

Rate of the LFO for the highpass filter

Source: `packages/core/controls.mjs`.

### hprelease

**Call:** `.hprelease(release)`. Alias: `hpr`.

Sets the release time for the highpass filter envelope.

```js
note("c2 e2 f2 g2")
.sound('sawtooth')
.clip(.5)
.hpf(500)
.hpenv(4)
.hpr("<.5 .25 .1 0>/4")
.release(.5)
```

Source: `packages/core/controls.mjs`.

### hpshape

**Call:** `.hpshape(shape)`.

Shape of the LFO for the highpass filter

Source: `packages/core/controls.mjs`.

### hpskew

**Call:** `.hpskew(skew)`.

Skew of the LFO for the highpass filter

Source: `packages/core/controls.mjs`.

### hpsustain

**Call:** `.hpsustain(sustain)`. Alias: `hps`.

Sets the sustain amplitude for the highpass filter envelope.

```js
note("c2 e2 f2 g2")
.sound('sawtooth')
.hpf(500)
.hpd(.5)
.hps("<0 .25 .5 1>/4")
.hpenv(4)
```

Source: `packages/core/controls.mjs`.

### hpsync

**Call:** `.hpsync(rate)`.

Cycle-synced rate of the LFO for the highpass filter

Source: `packages/core/controls.mjs`.

### hresonance

**Call:** `.hresonance(q)`. Same as `hpq`.

Controls the **h**igh-**p**ass **q**-value.

```js
s("bd sd [~ bd] sd,hh*8").hpf(2000).hpq("<0 10 20 30>")
```

Source: `packages/core/controls.mjs`.

### hsl

**Call:** `.hsl(hue, saturation, lightness)`.

Sets the pattern's color to the given [hsl](https://www.w3schools.com/htmL/html_colors_hsl.asp)

Source: `packages/core/pattern.mjs`.

### hsla

**Call:** `.hsla(hue, saturation, lightness, alpha)`.

Sets the pattern's color to the given [hsla](https://www.w3schools.com/htmL/html_colors_hsl.asp)

Source: `packages/core/pattern.mjs`.

### hurry

**Call:** `.hurry()`.

Both speeds up the pattern (like 'fast') and the sample playback (like 'speed').


s("bd sd:2").hurry("<1 2 4 3>").slow(1.5)

Source: `packages/core/pattern.mjs`.
