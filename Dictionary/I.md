### I

- `i`
- `imag`
- `inhabit`
- `inhabitmod`
- `initDough`
- `inside`
- `into`
- `inv`
- `invert`
- `ir`
- `irand`
- `irbegin`
- `iresponse`
- `irspeed`
- `isobite`
- `iter`
- `iterBack`
- `iterback`

## Entries

### i

**Call:** `.i(value)`.

Selects the given degree. Currently used in `xen` and `tune`:

```js
i("0 1 2 3 4 5 6 7").xen("<5edo 10edo 15edo hexany15>")
```

Source: `packages/core/controls.mjs`.

### imag

**Call:** `.imag(amount)`.

Imaginary part of a spectrum, registered as a pair with `real`. The browser synth does not read this control. It is registered with the other SuperDirt effects, next to `waveloss`.

```js
note("c3").s("sawtooth").imag("<0 .5 1>").osc().gain(0.15)
```

Source: `packages/core/controls.mjs`.

### inhabit

**Call:** `.inhabit(pat, xs)`. Alias: `pickSqueeze`.

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

### inhabitmod

**Call:** `.inhabitmod(pat, xs)`. Alias: `pickmodSqueeze`.

The same as `inhabit`, but if you pick a number greater than the size of the list,
it wraps around, rather than sticking at the maximum value.
For example, if you pick the fifth pattern of a list of three, you'll get the
second one.

Source: `packages/core/pick.mjs`.

### initDough

**Call:** `initDough`.

initializes dough ahead of time. you don't need to use this, but if you do, you can await it, so dough is ready before the pattern starts.

```js
await initDough()
$: chord("<Dm9 Dm11 Dm7>").offset("<-1 0 1 0>").voicing()
.phaser(3).fm(1.4).fmh(1.01)
.dough()
```

Source: `packages/dough/dough.mjs`.

### inside

**Call:** `.inside(cycles, func)`.

Slows the pattern by `cycles`, runs `func` on that longer span, then speeds it back. The function therefore sees several cycles as one.

```js
"0 1 2 3 4 3 2 1".inside(4, rev).scale("C:major").note().s("triangle").gain(0.2)
```

Source: `packages/core/pattern.mjs`.

### into

**Call:** `.into(…)`.

Breaks a pattern into pieces according to the structure of a given pattern.
True values in the given pattern cause the corresponding subcycle of the
source pattern to be looped, and for an (optional) given function to be
applied. False values result in the corresponding part of the source pattern
to be played unchanged.

```js
sound("bd sd ht lt").into("1 0", hurry(2))
```

Source: `packages/core/pattern.mjs`.

### inv

**Call:** `.inv()`. Same as `invert`.

Swaps 1s and 0s in a binary pattern.

```js
s("bd").struct("1 0 0 1 0 0 1 0".lastOf(4, invert))
```

Source: `packages/core/pattern.mjs`.

### invert

**Call:** `.invert()`. Alias: `inv`.

Swaps 1s and 0s in a binary pattern.

```js
s("bd").struct("1 0 0 1 0 0 1 0".lastOf(4, invert))
```

Source: `packages/core/pattern.mjs`.

### ir

**Call:** `.ir(sample)`. Alias: `irbegin`. Same as `iresponse`.

Sets the sample to use as an impulse response for the reverb.

```js
s("bd sd [~ bd] sd").room(.8).ir("<shaker_large:0 shaker_large:2>")
```

Source: `packages/core/controls.mjs`.

### irand

**Call:** `irand(n)`.

A continuous pattern of random integers, between 0 and n-1.

```js
// randomly select scale notes from 0 - 7 (= C to C)
n(irand(8)).struct("x x*2 x x*3").scale("C:minor")
```

Source: `packages/core/signal.mjs`.

### irbegin

**Call:** `.irbegin(begin)`. Alias: `ir`.

Sets the beginning of the IR response sample

```js
samples('github:switchangel/pad')
$: s("brk/2").fit().scrub(irand(16).div(16).seg(8)).ir("swpad:4").room(.65).irspeed("-2").irbegin("<0 .5 .75>/2").roomsize(.6)
```

Source: `packages/core/controls.mjs`.

### iresponse

**Call:** `iresponse(sample)`. Alias: `ir`.

Sets the sample to use as an impulse response for the reverb.

```js
s("bd sd [~ bd] sd").room(.8).ir("<shaker_large:0 shaker_large:2>")
```

Source: `packages/core/controls.mjs`.

### irspeed

**Call:** `.irspeed(speed)`.

Sets speed of the sample for the impulse response.

```js
samples('github:switchangel/pad')
$: s("brk/2").fit().scrub(irand(16).div(16).seg(8)).ir("swpad:4").room(.2).irspeed("<2 1 .5>/2").irbegin(.5).roomsize(.5)
```

Source: `packages/core/controls.mjs`.

### isobite

**Call:** `.isobite(structure)`. Aliases: `cycleStruct`, `cyclestruct`.

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

### iter

**Call:** `.iter(…)`.

Divides a pattern into a given number of subdivisions, plays the subdivisions in order, but increments the starting subdivision each cycle. The pattern wraps to the first subdivision after the last subdivision is played.

```js
note("0 1 2 3".scale('A minor')).iter(4)
```

Source: `packages/core/pattern.mjs`.

### iterBack

**Call:** `.iterBack(…)`. Alias: `iterback`.

Like `iter`, but plays the subdivisions in reverse order. Known as iter' in tidalcycles

```js
note("0 1 2 3".scale('A minor')).iterBack(4)
```

Source: `packages/core/pattern.mjs`.

### iterback

**Call:** `.iterback()`. Same as `iterBack`.

Like `iter`, but plays the subdivisions in reverse order. Known as iter' in tidalcycles

```js
note("0 1 2 3".scale('A minor')).iterBack(4)
```

Source: `packages/core/pattern.mjs`.
