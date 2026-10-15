### O

- `o` — alias of `orbit`
- `oct` — alias of `octave`
- `octave`
- `octaveR`
- `octaves`
- `octer`
- `octersub`
- `octersubsub`
- `off`
- `offset`
- `often`
- `onSchedule`
- `onTriggerTime`
- `or`
- `orbit`
- `oriA` — alias of `orientationAlpha`
- `oriB` — alias of `orientationBeta`
- `orientationAlpha`
- `orientationBeta`
- `orientationGamma`
- `orientationX` — alias of `orientationBeta`
- `orientationY` — alias of `orientationGamma`
- `orientationZ` — alias of `orientationAlpha`
- `oriG` — alias of `orientationGamma`
- `oriX` — alias of `orientationBeta`
- `oriY` — alias of `orientationGamma`
- `oriZ` — alias of `orientationAlpha`
- `osc`
- `oschost`
- `oscport`
- `outside`
- `overgain`
- `overshape`

## Entries

### octave

**Call:** `.octave(octave)`. Alias: `oct`.

Sets the default octave of a synth.

```js
n("0,4,7").scale("F:minor").s('supersaw').octave("<0 1 2 3>")
```

Source: `packages/core/controls.mjs`.

### octaveR

**Call:** `.octaveR(amount)`.

Registered control. The source says it was not found in the Tidal documentation, and this checkout does not apply it. The documented octave control is `octave`.

```js
n("0 2 4").scale("C:major").octaveR(1).s("triangle").gain(0.2)
```

Source: `packages/core/controls.mjs`.

### octaves

**Call:** `.octaves(count)`.

How many octaves apart the steps of a chord voicing are spread. The default is 1.

```js
chord("<Am C D F Am E Am E>").octaves("<1 2>").voicing().s("triangle").gain(0.15)
```

Source: `packages/core/controls.mjs`.

### octer

**Call:** `.octer(mix)`.

Octave-up mix. The browser synth does not read this control. It is registered with the other SuperDirt effects, next to `waveloss`.

```js
note("c3").s("sawtooth").octer("<0 .4 .8>").osc().gain(0.15)
```

Source: `packages/core/controls.mjs`.

### octersub

**Call:** `.octersub(mix)`.

Sub-octave mix, one octave down. The browser synth does not read this control. It is registered with the other SuperDirt effects, next to `waveloss`.

```js
note("c3").s("sawtooth").octersub("<0 .4 .8>").osc().gain(0.15)
```

Source: `packages/core/controls.mjs`.

### octersubsub

**Call:** `.octersubsub(mix)`.

Mix two octaves down, beside `octersub`. The browser synth does not read this control. It is registered with the other SuperDirt effects, next to `waveloss`.

```js
note("c3").s("sawtooth").octersubsub("<0 .4 .8>").osc().gain(0.15)
```

Source: `packages/core/controls.mjs`.

### off

**Call:** `.off(time, func)`.

Superimposes the function result on top of the original pattern, delayed by the given time.

```js
"c3 eb3 g3".off(1/8, x=>x.add(7)).note()
```

Source: `packages/core/pattern.mjs`.

### offset

**Call:** `.offset(shift)`.

Sets how the voicing is offset from the anchored position

```js
chord("<Am C D F Am E Am E>").offset("<0 1 2 3 4 5>") // alter the voicing each time
```

Source: `packages/core/controls.mjs`.

### often

**Call:** `.often(…)`.

Shorthand for `.sometimesBy(0.75, fn)`

```js
s("hh*8").often(x=>x.speed("0.5"))
```

Source: `packages/core/signal.mjs`.

### onSchedule

**Call:** `.onSchedule(…)`.

Attaches a function that is called for each hap onset.

```js
s("bd sd").onSchedule((hap, time, cps) => {
  console.log('hap scheduled', time, cps);
})
```

Source: `packages/core/pattern.mjs`.

### onTriggerTime

**Call:** `.onTriggerTime(…)`.

make something happen on event time
uses browser timeout which is innacurate for audio tasks

```js
s("bd!8").onTriggerTime((hap) => {console.log(hap)})
```

Source: `packages/core/pattern.mjs`.

### or

**Call:** `or(a, b)`.

performs a || b

Source: `packages/core/pattern.mjs`.

### orbit

**Call:** `.orbit(number)`. Alias: `o`.

An `orbit` is a global parameter context for patterns. Patterns with the same orbit will share the same global effects.

```js
stack(
  s("hh*6").delay(.5).delaytime(.25).orbit(1),
  s("~ sd ~ sd").delay(.5).delaytime(.125).orbit(2)
)
```

Source: `packages/core/controls.mjs`.

### orientationAlpha

**Call:** `orientationAlpha`. Aliases: `oriA`, `oriZ`, `orientationZ`.

The device's orientation alpha value ranges from 0 to 1.

```js
n(orientationAlpha.segment(4).range(0,7)).scale("C:minor")
```

Source: `packages/motion/motion.mjs`.

### orientationBeta

**Call:** `orientationBeta`. Aliases: `oriB`, `oriX`, `orientationX`.

The device's orientation beta value ranges from 0 to 1.

```js
n(orientationBeta.segment(4).range(0,7)).scale("C:minor")
```

Source: `packages/motion/motion.mjs`.

### orientationGamma

**Call:** `orientationGamma`. Aliases: `oriG`, `oriY`, `orientationY`.

The device's orientation gamma value ranges from 0 to 1.

```js
n(orientationGamma.segment(4).range(0,7)).scale("C:minor")
```

Source: `packages/motion/motion.mjs`.

### osc

**Call:** `.osc()`.

Sends each hap as an OSC message, which can be picked up by SuperCollider or any other OSC-enabled software.
For more info, read [MIDI & OSC in the docs](https://strudel.cc/learn/input-output/)

Source: `packages/osc/osc.mjs`.

### oschost

**Call:** `.oschost(oschost)`.

The host to send open sound control messages to. Requires running the OSC bridge.

```js
note("c4").oschost('127.0.0.1').oscport(57120).osc();
```

Source: `packages/core/controls.mjs`.

### oscport

**Call:** `.oscport(oscport)`.

The port to send open sound control messages to. Requires running the OSC bridge.

```js
note("c4").oschost('127.0.0.1').oscport(57120).osc();
```

Source: `packages/core/controls.mjs`.

### outside

**Call:** `.outside(cycles, func)`.

Speeds the pattern by `cycles`, runs `func`, then slows it back. The function therefore treats one cycle as several.

```js
"<[0 1] 2 [3 4] 5>".outside(4, rev).scale("C:major").note().s("triangle").gain(0.2)
```

Source: `packages/core/pattern.mjs`.

### overgain

**Call:** `.overgain(amount)`.

Gain past the usual limit. The source says normal gain is limited to 2, and this control is what lets a value go higher. The browser synth does not read it.

```js
s("bd*4").overgain(3).osc()
```

Source: `packages/core/controls.mjs`.

### overshape

**Call:** `.overshape(amount)`.

Registered next to `overgain`. The source says it is the same kind of override, with a limit of 1. The browser waveshaper reads `shape` and `shapevol`, not this control.

```js
note("c3").s("sawtooth").overshape(0.8).gain(0.15)
```

Source: `packages/core/controls.mjs`.
