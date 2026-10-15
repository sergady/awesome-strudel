### M

- `markcss`
- `midibend`
- `midichan`
- `midicmd`
- `midikeys`
- `midimap`
- `midin`
- `midiport`
- `miditouch`
- `minutes`
- `mod`
- `mode`
- `mousex`
- `mouseX` — alias of `mousex`
- `mousey`
- `mouseY` — alias of `mousey`
- `moveXY`
- `mtranspose`
- `mul`

## Entries

### markcss

**Call:** `.markcss(…)`.

Overrides the css of highlighted events. Make sure to use single quotes!

```js
note("c a f e")
.markcss('text-decoration:underline')
```

Source: `packages/codemirror/codemirror.mjs`.

### midibend

**Call:** `.midibend(midibend)`.

MIDI pitch bend: Sends a MIDI pitch bend message.

```js
note("c4").midibend(sine.slow(4).range(-0.4,0.4)).midi()
```

Source: `packages/core/controls.mjs`.

### midichan

**Call:** `.midichan(channel)`.

MIDI channel: Sets the MIDI channel for the event.

```js
note("c4").midichan(1).midi()
```

Source: `packages/core/controls.mjs`.

### midicmd

**Call:** `.midicmd(command)`.

MIDI command: Sends a MIDI command message.

```js
midicmd("clock*48,<start stop>/2").midi()
```

Source: `packages/core/controls.mjs`.

### midikeys

**Call:** `midikeys(input)`.

MIDI keyboard: Opens a MIDI input port to receive MIDI keyboard messages.

The note length is fixed as Superdough is not currently set up for undetermined
note durations

The 'midichan' control value contains the number of the channel the note is coming from
so it could be filtered or manipulated further in the chain.

```js
const kb = await midikeys('Arturia KeyStep 32')
kb().s("tri").lpf(80).lpe(6).lpd(0.1).room(2).delay(0.35)
```

```js
const kb = await midikeys('Arturia KeyStep 32')
kb("0.5 1")
  .s("saw")
  .add(note(rand.mul(0.3)))
  .lpf(1000).lpe(2).room(0.5)
```

```js
// discard all notes not coming out from midi channel 2
const kb = await midikeys('Arturia KeyStep 32')
kb().filterValues(v=>v.midichan==2).s("tri")
```

Source: `packages/midi/midi.mjs`.

### midimap

**Call:** `.midimap(name)`.

Selects a named MIDI map. A map connects control names such as `lpf` to MIDI controller numbers. Register maps with `midimaps`, then send them with `.midi()`. The default name is `default`.

```js
note("c4").lpf(800).midimap("mymap").midi()
```

Source: `packages/core/controls.mjs`.

### midin

**Call:** `midin(input)`.

MIDI input: Opens a MIDI input port to receive MIDI control change messages.

The output is a function that accepts a midi cc value to query as well as (optionally) a midi channel

```js
const cc = await midin('IAC Driver Bus 1')
note("c a f e").lpf(cc(0).range(0, 1000)).lpq(cc(1).range(0, 10)).sound("sawtooth")
```

```js
const allCC = await midin('IAC Driver Bus 1')
const cc = (ccNum) => allCC(ccNum, 2) // just channel 2
note("c a f e").s("saw")
  .when(cc(0).gt(0), x => x.postgain(0))
```

Source: `packages/midi/midi.mjs`.

### midiport

**Call:** `.midiport(port)`.

MIDI port: Sets the MIDI port for the event.

```js
note("c a f e").midiport("<0 1 2 3>").midi()
```

Source: `packages/core/controls.mjs`.

### miditouch

**Call:** `.miditouch(miditouch)`.

MIDI key after touch: Sends a MIDI key after touch message.

```js
note("c4").miditouch(sine.slow(4).range(0,1)).midi()
```

Source: `packages/core/controls.mjs`.

### minutes

**Call:** `.minutes(count)`.

Registered with `hours`, `seconds`, and `songPtr` as clock metadata. This checkout does not apply it.

```js
note("c4").s("triangle").minutes(0).gain(0.2)
```

Source: `packages/core/controls.mjs`.

### mod

**Call:** `mod`.

Divides each number by the given factor and returns the remainder

Source: `packages/core/pattern.mjs`.

### mode

**Call:** `.mode(modeName)`.

How the voicing is aligned to the anchor
  - `below`: top note <= anchor
  - `duck`: top note <= anchor, anchor excluded
  - `above`: bottom note >= anchor
  - `root`: bottom note is the lowest root of the chord >= anchor

  - `oldabove` : old (buggy) behavior of above, kept for legacy reason
  - `oldroot` : old (buggy) behavior of root, kept for legacy reason

```js
mode("<below above duck root>").chord("C").voicing()
```

Source: `packages/core/controls.mjs`.

### mousex

**Call:** `mousex`. Alias: `mouseX`.

The mouse's x position value ranges from 0 to 1.

```js
n(mousex.segment(4).range(0,7)).scale("C:minor")
```

Source: `packages/core/signal.mjs`.

### mousey

**Call:** `mousey`. Alias: `mouseY`.

The mouse's y position value ranges from 0 to 1.

```js
n(mousey.segment(4).range(0,7)).scale("C:minor")
```

Source: `packages/core/signal.mjs`.

### moveXY

**Call:** `.moveXY(dx, dy)`.

Adds `dx` to the drawing `x` and `dy` to the drawing `y`.

```js
s("rect").x(0.2).y(0.2).w(0.3).h(0.3).moveXY("<0 .2>", 0)
```

Source: `packages/draw/animate.mjs`.

### mtranspose

**Call:** `.mtranspose(amount)`.

Registered control. The source says it was not found in the Tidal documentation, and this checkout does not apply it.

```js
note("c4 e4 g4").s("triangle").mtranspose(1).gain(0.2)
```

Source: `packages/core/controls.mjs`.

### mul

**Call:** `.mul(…)`.

Multiplies each number by the given factor.

```js
"<1 1.5 [1.66, <2 2.33>]>*4".mul(150).freq()
```

Source: `packages/core/pattern.mjs`.
