#!/usr/bin/env python3
"""Fill dictionary entries that had no source description or example."""
import re
from pathlib import Path

ROOT = Path("/home/sergady/Documents/GIT/awesome-strudel/Dictionary")

def dirt(meaning):
    return (
        f"{meaning} The browser synth does not read this control. "
        "It is registered with the other SuperDirt effects, next to `waveloss`."
    )

ENTRIES = {
"comb": (".comb(mix)", dirt("Comb-filter mix."), 'note("c3").s("sawtooth").comb("<0 .4 .8>").osc().gain(0.15)'),
"compressorAttack": (".compressorAttack(seconds)", "How many seconds the compressor takes to start reducing gain after the signal passes the threshold. `compressor` sets that threshold. Attack, knee, ratio, and release are the Web Audio compressor parameters.", 'note("c3*4").s("sawtooth").compressor(-24).compressorRatio(8).compressorAttack("<0.005 .2>").gain(0.15)'),
"compressorKnee": (".compressorKnee(decibels)", "Width, in decibels, of the knee where compression begins. A wider knee eases into the reduction instead of switching it on at the threshold.", 'note("c3*4").s("sawtooth").compressor(-18).compressorKnee("<0 10 30>").gain(0.15)'),
"compressorRatio": (".compressorRatio(ratio)", "How strongly the compressor turns the signal down once it is past the threshold. Higher ratios squash the peaks more.", 'note("c3*8").s("sawtooth").gain("<0.05 0.4>").compressor(-12).compressorRatio("<1 4 12>")'),
"compressorRelease": (".compressorRelease(seconds)", "How many seconds the compressor takes to let go after the signal falls back under the threshold.", 'note("c3*2").s("sawtooth").compressor(-20).compressorRatio(6).compressorRelease("<0.05 .4>").gain(0.15)'),
"compressSpan": (".compressSpan(span)", "Same work as `compress`: fit the pattern between two points in the cycle. The two points are `span.begin` and `span.end` on one value. `compressspan` is the same function.", 's("bd sd").compress(0.25, 0.75)'),
"compressspan": (".compressspan(span)", "Same function as `compressSpan`. It reads `begin` and `end` from one value and fits the pattern into that slice of the cycle.", 's("bd sd").compressspan({begin: 0.25, end: 0.75})'),
"cpm": (".cpm(cyclesPerMinute)", "Plays this pattern at the given number of cycles per minute. In the editor, that is relative to the clock already set by `setcpm` or `setcps`. The copy in `pattern.mjs` is marked deprecated and assumes one cycle per second.", 's("<bd sd>,hh*2").cpm(90)'),
"cps": (".cps(cyclesPerSecond)", "Writes a cycles-per-second value onto the event. It does not change the editor clock. The clock functions are `setcps` and `setcpm`. This control is registered with the other playback-metadata controls (`hours`, `minutes`, `seconds`, `songPtr`).", 'note("c4*4").s("triangle").cps(0.5).gain(0.2)'),
"csound": (".csound(instrument)", "Sends each event to a Csound instrument. The instrument name defaults to `triangle`. `@strudel/csound` is not loaded by the default editor prebake.", 'note("c4 e4 g4").csound("triangle").gain(0.2)'),
"ctlNum": (".ctlNum(number)", "A MIDI controller-number control. The MIDI output in this checkout sends `ccn` together with `ccv`, and does not read `ctlNum`.", 'note("c4").ctlNum(74).ccv(0.5).midi()'),
"ctranspose": (".ctranspose(amount)", "Registered control. The source says it was not found in the Tidal documentation, and this checkout does not apply it.", 'note("c4 e4 g4").s("triangle").ctranspose(1).gain(0.2)'),
"curve": (".curve(amount)", "Waveshape curve of a ZZFX sound (`zzfx`, `z_sine`, `z_sawtooth`, and the other `z_` names). The synth raises the waveform to this power. The ZZFX comment treats 0 as square and 2 as pointy. A square ZZFX wave forces the curve to 0.", 's("z_sawtooth").note("c3").curve("<0 1 2>").gain(0.2)'),
"degree": (".degree(amount)", "Registered control. The source says it was not found in the Tidal documentation, and this checkout does not apply it.", 'n("0 2 4").scale("C:major").degree(1).s("triangle").gain(0.2)'),
"deltaSlide": (".deltaSlide(amount)", "Pitch acceleration of a ZZFX sound. `slide` is the pitch glide, and this value changes that glide while the sound plays.", 's("z_sine").note("c3").slide(0.2).deltaSlide("<0 1 3>").gain(0.2)'),
"enhance": (".enhance(amount)", dirt("Spectral enhance."), 'note("c3").s("sawtooth").enhance("<0 .5 1>").osc().gain(0.15)'),
"euclidrot": (".euclidrot(pulses, steps, rotation)", "Same function as `euclidRot`. Distributes `pulses` across `steps` as evenly as possible, then rotates the pattern by `rotation` steps.", 'note("c3").s("triangle").euclidrot(3, 8, 1).decay(0.08).sustain(0).gain(0.2)'),
"expression": (".expression(amount)", "MIDI expression control. It is registered next to `sustainpedal`. The MIDI output in this checkout does not send it.", 'note("c4 e4 g4").expression(0.7).midi()'),
"fadeInTime": (".fadeInTime(time)", "Registered beside `fadeTime`, the fade-out of a chopped or sliced grain. This is the matching fade-in control. The source documents `fadeTime` only, and the browser synth does not read `fadeInTime`.", 's("bd*4").begin(0.2).fadeInTime("<0 .2 .5>")'),
"fft": (".fft(size)", "Exponent for the analyser window used by `analyze`. The window length is `2 ** (fft + 5)`. The default is 8, which is 8192 samples. Values run from 0 to 10.", 'note("c3 e3 g3").s("sawtooth").analyze(1).fft("<5 8 10>").gain(0.15)'),
"focus": (".focus(begin, end)", "Fits the whole pattern between two cycle positions and does not leave the rest of the cycle empty. The focused span can be longer than one cycle, unlike `compress`.", 's("bd hh sd hh").focus(1/4, 3/4)'),
"focusSpan": (".focusSpan(span)", "Same function as `focus`, reading `begin` and `end` from one value. `focusspan` is the same function.", 's("bd hh sd hh").focus(0.25, 0.75)'),
"focusspan": (".focusspan(span)", "Same function as `focusSpan`.", 's("bd hh sd hh").focusspan({begin: 0.25, end: 0.75})'),
"frameRate": (".frameRate(rate)", "Registered with the playback-metadata controls (`frames`, `hours`, `minutes`, `seconds`, `songPtr`). This checkout does not apply it.", 'note("c4").s("triangle").frameRate(30).gain(0.2)'),
"frames": (".frames(count)", "Registered with `frameRate` and the clock-metadata controls. This checkout does not apply it.", 'note("c4").s("triangle").frames(16).gain(0.2)'),
"freeze": (".freeze(amount)", dirt("Spectral freeze, holding the current spectrum."), 'note("c3").s("sawtooth").freeze("<0 1>").osc().gain(0.15)'),
"fshift": (".fshift(amount)", dirt("Frequency shift."), 'note("c3").s("sawtooth").fshift("<0 20 80>").osc().gain(0.15)'),
"fshiftnote": (".fshiftnote(steps)", dirt("Frequency shift in note steps, beside `fshift`."), 'note("c3").s("sawtooth").fshiftnote("<0 7 12>").osc().gain(0.15)'),
"fshiftphase": (".fshiftphase(phase)", dirt("Phase of the frequency shifter, beside `fshift`."), 'note("c3").s("sawtooth").fshift(40).fshiftphase("<0 .5 1>").osc().gain(0.15)'),
"FXrelease": (".FXrelease(seconds)", "How long effects keep running after the note, in seconds. The played release is the longer of this value and `release`. Alias spellings `FXrel`, `FXr`, and `fxr` are the same control.", 'note("c3 ~").s("sawtooth").release(0.05).room(0.4).FXrelease("<0.05 1>").gain(0.15)'),
"gate": (".gate(level)", "Gate control, with alias `gat`. The source points at Tidal's control-voltage gate. The browser synth does not read it.", 'note("c4*4").s("triangle").gate("<1 0>").gain(0.2)'),
"getClockTime": ("getClockTime()", "Returns the scheduler's current clock time in seconds, the same clock `onSchedule` uses. It throws if playback has not set a clock.", "getClockTime()"),
"getCps": ("getCps()", "Returns the scheduler's current cycles per second. `setcps` and `setcpm` are what change it.", "getCps()"),
"getTime": ("getTime()", "Returns the scheduler's current time in cycles. It throws if playback has not set a time source.", "getTime()"),
"glide": (".glide(amount)", "Dough control registered beside `group` and `voices`. The source does not define the glide time, and the browser synth does not read it.", 'note("c3 e3 g3").s("sawtooth").glide(0.1).gain(0.15)'),
"group": (".group(id)", "Group id used by dough. `groupmod` copies this id onto a modulator so dough can update that group.", 'note("c3 e3 g3").s("sawtooth").group(1).gain(0.15)'),
"groupmod": (".groupmod(modulator)", "Stacks the pattern with a dough update. The modulator events keep the pattern's `group` id and are marked `dough: 'update_group'`. `gmod` is the same method. This is for the dough backend.", 'note("c3").s("sawtooth").group(1).groupmod(note("g3").gain(0.1))'),
"harmonic": (".harmonic(amount)", "Registered control. The source says it was not found in the Tidal documentation, and this checkout does not apply it.", 'note("c4").s("triangle").harmonic(2).gain(0.2)'),
"hbrick": (".hbrick(frequency)", dirt("High brickwall cutoff."), 'note("c3").s("sawtooth").hbrick("<2000 8000>").osc().gain(0.15)'),
"hold": (".hold(time)", "Registered beside `release`, with no further comment. The browser envelope uses `attack`, `decay`, `sustain`, and `release`, and does not read `hold`.", 'note("c4 e4 g4").s("triangle").hold(0.2).gain(0.2)'),
"hours": (".hours(count)", "Registered with `minutes`, `seconds`, and `songPtr` as clock metadata. This checkout does not apply it.", 'note("c4").s("triangle").hours(0).gain(0.2)'),
"imag": (".imag(amount)", dirt("Imaginary part of a spectrum, registered as a pair with `real`."), 'note("c3").s("sawtooth").imag("<0 .5 1>").osc().gain(0.15)'),
"inside": (".inside(cycles, func)", "Slows the pattern by `cycles`, runs `func` on that longer span, then speeds it back. The function therefore sees several cycles as one.", '"0 1 2 3 4 3 2 1".inside(4, rev).scale("C:major").note().s("triangle").gain(0.2)'),
"kcutoff": (".kcutoff(frequency)", dirt("Low-pass cutoff that follows `krush`."), 'note("c3").s("sawtooth").krush(0.5).kcutoff("<500 4000>").osc().gain(0.15)'),
"krush": (".krush(amount)", dirt("Bit-crushing."), 'note("c3 e3 g3").s("sawtooth").krush("<0 .3 .7>").osc().gain(0.15)'),
"lbrick": (".lbrick(frequency)", dirt("Low brickwall cutoff."), 'note("c3").s("sawtooth").lbrick("<100 800>").osc().gain(0.15)'),
"log2": (".log2()", "Base-2 logarithm of each number. 1, 2, 4, 8 become 0, 1, 2, 3.", 'n("1 2 4 8".log2()).scale("C4:major").s("triangle").gain(0.2)'),
"loopat": (".loopat(cycles)", "Same function as `loopAt`. Changes the sample speed so the sample lasts the given number of cycles.", 's("piano").loopat(4)'),
"loopatcps": (".loopatcps(cycles, cps)", "Same function as `loopAtCps`. Fits the sample to `cycles` at the given cycles per second. The source marks it deprecated in favor of `loopAt` or `fit` together with `setcps`.", 's("piano").loopatcps(4, 0.5)'),
"midimap": (".midimap(name)", "Selects a named MIDI map. A map connects control names such as `lpf` to MIDI controller numbers. Register maps with `midimaps`, then send them with `.midi()`. The default name is `default`.", 'note("c4").lpf(800).midimap("mymap").midi()'),
"minutes": (".minutes(count)", "Registered with `hours`, `seconds`, and `songPtr` as clock metadata. This checkout does not apply it.", 'note("c4").s("triangle").minutes(0).gain(0.2)'),
"moveXY": (".moveXY(dx, dy)", "Adds `dx` to the drawing `x` and `dy` to the drawing `y`.", 's("rect").x(0.2).y(0.2).w(0.3).h(0.3).moveXY("<0 .2>", 0)'),
"mtranspose": (".mtranspose(amount)", "Registered control. The source says it was not found in the Tidal documentation, and this checkout does not apply it.", 'note("c4 e4 g4").s("triangle").mtranspose(1).gain(0.2)'),
"nudge": (".nudge(seconds)", "Delays the outgoing OSC message by this many seconds. The source says it cannot be negative beyond the latency, which is why it is not the same control as `early` or `late`. The browser synth does not read it.", 's("bd*4").nudge(0.05).osc()'),
"octaveR": (".octaveR(amount)", "Registered control. The source says it was not found in the Tidal documentation, and this checkout does not apply it. The documented octave control is `octave`.", 'n("0 2 4").scale("C:major").octaveR(1).s("triangle").gain(0.2)'),
"octaves": (".octaves(count)", "How many octaves apart the steps of a chord voicing are spread. The default is 1.", 'chord("<Am C D F Am E Am E>").octaves("<1 2>").voicing().s("triangle").gain(0.15)'),
"octer": (".octer(mix)", dirt("Octave-up mix."), 'note("c3").s("sawtooth").octer("<0 .4 .8>").osc().gain(0.15)'),
"octersub": (".octersub(mix)", dirt("Sub-octave mix, one octave down."), 'note("c3").s("sawtooth").octersub("<0 .4 .8>").osc().gain(0.15)'),
"octersubsub": (".octersubsub(mix)", dirt("Mix two octaves down, beside `octersub`."), 'note("c3").s("sawtooth").octersubsub("<0 .4 .8>").osc().gain(0.15)'),
"outside": (".outside(cycles, func)", "Speeds the pattern by `cycles`, runs `func`, then slows it back. The function therefore treats one cycle as several.", '"<[0 1] 2 [3 4] 5>".outside(4, rev).scale("C:major").note().s("triangle").gain(0.2)'),
"overgain": (".overgain(amount)", "Gain past the usual limit. The source says normal gain is limited to 2, and this control is what lets a value go higher. The browser synth does not read it.", 's("bd*4").overgain(3).osc()'),
"overshape": (".overshape(amount)", "Registered next to `overgain`. The source says it is the same kind of override, with a limit of 1. The browser waveshaper reads `shape` and `shapevol`, not this control.", 'note("c3").s("sawtooth").overshape(0.8).gain(0.15)'),
"panorient": (".panorient(direction)", "Registered beside `pan`, `panspan`, and `pansplay`. The browser synth reads `pan` only, not this control.", 's("bd*4").pan("<0 1>").panorient(0.5)'),
"panwidth": (".panwidth(width)", "Registered beside `pansplay`. The browser synth reads `pan` only, not this control.", 's("bd*4").pan("<0 1>").panwidth("<0.2 1>")'),
"phaserrate": (".phaserrate(hertz)", "Speed of the phaser's tremolo, in hertz. The phaser is built only when `phaserdepth` is greater than 0.", 'note("c3").s("sawtooth").phaserdepth(0.8).phaserrate("<0.2 2 6>").gain(0.12)'),
"pick": (".pick(list)", "Uses each value as an index into a list or object of patterns, and plays the chosen pattern. The index keeps the time structure of the index pattern.", 'sound("<0 1 [2,0]>".pick(["bd sd", "cp cp", "hh hh"]))'),
"pitchJump": (".pitchJump(amount)", "Size of a one-time pitch jump in a ZZFX sound. `pitchJumpTime` is when that jump happens.", 's("z_sine").note("c3").pitchJump("<0 200 600>").pitchJumpTime(0.1).gain(0.2)'),
"pitchJumpTime": (".pitchJumpTime(time)", "When the ZZFX `pitchJump` happens, as the synth's time parameter.", 's("z_sawtooth").note("c3").pitchJump(400).pitchJumpTime("<0.02 .1 .2>").gain(0.2)'),
"polyTouch": (".polyTouch(pressure)", "Polyphonic aftertouch for a MIDI note. The MIDI output reads the value off the event and does not send a polyphonic-aftertouch message.", 'note("c4 e4 g4").polyTouch("<0 .5 1>").midi()'),
"psustain": (".psustain(level)", "Sustain level of the pitch envelope. `pattack`, `pdecay`, and `prelease` are the other times. The pitch envelope also needs `penv` if the pitch is going to move. Alias: `psus`.", 'note("c3 eb3 g3").s("sawtooth").penv(12).psustain("<0 .5 1>").gain(0.15)'),
"real": (".real(amount)", dirt("Real part of a spectrum, registered as a pair with `imag`."), 'note("c3").s("sawtooth").real("<0 .5 1>").osc().gain(0.15)'),
"rescale": (".rescale(factor)", "Multiplies the drawing controls `x`, `y`, `w`, and `h` by the same factor.", 's("rect").x(0.25).y(0.25).w(0.5).h(0.5).rescale("<1 .5 .25>")'),
"ring": (".ring(mix)", dirt("Ring-modulation mix."), 'note("c3").s("sawtooth").ring("<0 .4 .8>").osc().gain(0.15)'),
"ringdf": (".ringdf(amount)", dirt("A ring-modulation control registered with `ring` and `ringf`."), 'note("c3").s("sawtooth").ring(0.6).ringf(200).ringdf("<0 20 80>").osc().gain(0.15)'),
"ringf": (".ringf(frequency)", dirt("Ring-modulation frequency."), 'note("c3").s("sawtooth").ring(0.7).ringf("<50 200 700>").osc().gain(0.15)'),
"scram": (".scram(amount)", dirt("Scrambling of spectral bins."), 'note("c3").s("sawtooth").scram("<0 .4 .8>").osc().gain(0.15)'),
"seconds": (".seconds(count)", "Registered with `hours`, `minutes`, and `songPtr` as clock metadata. This checkout does not apply it.", 'note("c4").s("triangle").seconds(0).gain(0.2)'),
"semitone": (".semitone(steps)", "Registered next to `slide`. The source asks whether it is a detune and does not wire it to the browser synth. Pitch shift in the browser is `transpose`.", 'note("c4 e4 g4").s("triangle").semitone(1).gain(0.2)'),
"shapevol": (".shapevol(gain)", "Gain after the waveshaper. `shape` is the amount of shaping, and this is the level of the shaped signal. The default is 1.", 'note("c3").s("sawtooth").shape(0.6).shapevol("<0.2 1>").gain(0.15)'),
"slide": (".slide(amount)", "Pitch glide of a ZZFX sound. Positive values sweep the frequency while the note plays. `deltaSlide` then speeds that glide up or down. The same name is also registered as an undocumented synth parameter.", 's("z_sine").note("c3").slide("<0 .3 1>").gain(0.2)'),
"smear": (".smear(amount)", "Two registrations share this name. In `controls.mjs` it is a SuperDirt spectral smear, which the browser synth does not apply. In `draw/animate.mjs` it is a drawing parameter next to `x`, `y`, `w`, and `h`. Whichever package is loaded later owns the method.", 'note("c3").s("sawtooth").smear("<0 .5 1>").osc().gain(0.15)'),
"songPtr": (".songPtr(position)", "Registered with the clock-metadata controls. This checkout does not apply it.", 'note("c4").s("triangle").songPtr(0).gain(0.2)'),
"speak": (".speak(lang, voice)", "Speaks each event value with the browser speech synthesizer. `lang` is a language tag such as `en`. `voice` is an index into the voices for that language, or a voice name.", '"one two three four".speak("en", 0)'),
"stepsPerOctave": (".stepsPerOctave(count)", "Registered control. The source says it was not found in the Tidal documentation, and this checkout does not apply it.", 'n("0 2 4 6").scale("C:major").stepsPerOctave(12).s("triangle").gain(0.2)'),
"sustainpedal": (".sustainpedal(down)", "MIDI sustain-pedal control, registered next to `expression`. The MIDI output in this checkout does not send it.", 'note("c4 e4 g4 c5").sustainpedal("<0 1>").midi()'),
"transsustain": (".transsustain(level)", "Sustain emphasis of the transient shaper. `transient` is the attack emphasis, from -1 to 1, and this is the sustain emphasis on the same scale. A colon value to `transient` can set both, because they are registered together.", 's("hh*8").bank("RolandTR909").transient(0.4).transsustain("<-1 0 1>")'),
"triode": (".triode(amount)", dirt("Triode distortion."), 'note("c3").s("sawtooth").triode("<0 .4 .8>").osc().gain(0.15)'),
"tsdelay": (".tsdelay(time)", dirt("A delay registered with `xsdelay`."), 'note("c3 ~").s("sawtooth").tsdelay("<0 .2 .5>").osc().gain(0.15)'),
"tuning": (".tuning(ratios)", "Maps a numeric pattern through a list of frequency ratios. The index wraps, and each extra trip around the list multiplies the ratio by 2, so the list repeats at the octave. The source calls this an early version of `xen`. The result is a ratio, so multiply by a root frequency before `freq`.", 'n("0 1 2 3").tuning([1, 1.25, 1.5, 2]).mul(220).freq().s("triangle").gain(0.2)'),
"uid": (".uid(id)", "Registered with the playback-metadata controls. This checkout does not apply it.", 'note("c4").s("triangle").uid(1).gain(0.2)'),
"val": (".val(value)", "Registered with `uid`, `cps`, and `songPtr`. This checkout does not apply it.", 'note("c4").s("triangle").val(1).gain(0.2)'),
"vlpf": (".vlpf(frequency)", "Not exported. The name appears only as an example of `register`: a custom cutoff that multiplies the frequency by the event's velocity. Run the registration once, then call the new method.", 'const vlpf = register("vlpf", (freq, pat) => pat.fmap((v) => ({...v, cutoff: freq * (v.velocity ?? 1)})))\ns("sawtooth").seg(8).velocity(rand).vlpf(800).gain(0.15)'),
"voice": (".voice(name)", "Registered as a synth parameter, with no further definition. The browser synth does not read it. Dough voices are the separate `voices` control.", 'note("c4").s("triangle").voice(0).gain(0.2)'),
"voices": (".voices(count)", "Dough voice-count control, registered beside `group` and `glide`. The source does not say how the count is used.", 'note("c3 e3 g3").s("sawtooth").voices(4).gain(0.15)'),
"xsdelay": (".xsdelay(time)", dirt("A delay registered with `tsdelay`."), 'note("c3 ~").s("sawtooth").xsdelay("<0 .25 .5>").osc().gain(0.15)'),
"zcrush": (".zcrush(amount)", "Bit crush of a ZZFX sound. The source says it is like `crush`, scaled differently. It is one of the ZZFX parameters, not the general `crush` control.", 's("z_sawtooth").note("c3").zcrush("<0 4 10>").gain(0.2)'),
"zdelay": (".zdelay(time)", "Delay inside a ZZFX sound, in the synth's own time unit. It is not the pattern `delay` send.", 's("z_sine").note("c3").zdelay("<0 .05 .15>").gain(0.2)'),
"zmod": (".zmod(amount)", "Modulation amount of a ZZFX sound.", 's("z_sawtooth").note("c3").zmod("<0 .2 .6>").gain(0.2)'),
"znoise": (".znoise(amount)", "Noise mixed into a ZZFX sound. The source comment calls it frequency fog.", 's("z_sine").note("c3").znoise("<0 .2 .6>").gain(0.2)'),
"zoomArc": (".zoomArc(span)", "Same function as `zoom`, reading `begin` and `end` from one value. `zoomarc` is the same function. The slice is stretched to fill the cycle.", 'note("c4 d4 e4 f4 g4 a4").s("triangle").zoom(0, 0.5).gain(0.2)'),
"zoomarc": (".zoomarc(span)", "Same function as `zoomArc`.", 'note("c4 d4 e4 f4 g4 a4").s("triangle").zoomarc({begin: 0, end: 0.5}).gain(0.2)'),
"zoomIn": (".zoomIn(factor)", "Drawing zoom toward the center. It multiplies `x`, `y`, `w`, and `h` by `factor`, then shifts `x` and `y` by `(1 - factor) / 2`.", 's("rect").x(0.1).y(0.1).w(0.8).h(0.8).zoomIn("<1 .6 .3>")'),
"zrand": (".zrand(amount)", "Random detune of a ZZFX sound. The synth picks a frequency inside a range set by this amount.", 's("z_sine").note("c3*8").zrand("<0 .05 .3>").gain(0.2)'),
"zzfx": (".zzfx(params)", "Raw ZZFX parameter list. When it is set, it replaces the parameters built from `zrand`, `curve`, `slide`, `pitchJump`, `znoise`, `zmod`, `zcrush`, `zdelay`, and the envelope. Use it with `s(\"zzfx\")` or a `z_` waveform.", 's("zzfx").zzfx([0.2, 0, 220, 0, 0.1, 0.1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0.4, 0, 0]).gain(0.3)'),
}

missing = []
for path in sorted(ROOT.glob("*.md")):
    text = path.read_text()
    original = text
    for name, (call, desc, example) in ENTRIES.items():
        pat = rf"### {re.escape(name)}\n\n\*\*Call:\*\* [^\n]+\n\nNo description or example in this checkout\.\n"
        body = f"### {name}\n\n**Call:** `{call}`.\n\n{desc}\n\n```js\n{example}\n```\n"
        text, n = re.subn(pat, body, text, count=1)
        if n == 0 and f"### {name}\n" in text and "No description or example in this checkout." in text.split(f"### {name}\n", 1)[1][:400]:
            missing.append(f"{path.name}:{name}")
    if text != original:
        path.write_text(text)

print("unmatched", missing)
left = 0
for path in ROOT.glob("*.md"):
    left += path.read_text().count("No description or example in this checkout.")
print("remaining placeholders", left)
