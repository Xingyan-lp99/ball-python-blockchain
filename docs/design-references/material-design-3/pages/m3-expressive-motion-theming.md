# Adding Motion Physics with Jetpack Compose

Source: https://m3.material.io/m3-expressive-motion-theming
Content endpoint: https://m3.material.io/_dsm/content/m3/2026-11-17_08-50-14/db985439-a4b8-4b9e-bb86-6fb113b99d92.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Supercharge your Android transitions and animations with the new M3 Expressive motion theming system.

## Tab 1

#data-origin-author

<p><strong>Rebecca Franks</strong>, Developer Relations Engineer, Android</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4fn3jj-rebecca.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/pqB-aRpMXbp97_mqcDz3TQGTahy9rPkWMqiEJFvDqEWe5x5dXxtGLBqSQzOsGh0vADJ_fnsEiMzg9_3N4xYQY-Iy6cB3u6wRVbZTEdBkqK8o=s413

#data-origin-author

<p><strong>Austin Fisher</strong>, Sr. UX Content Designer</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4foytq-austin.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/A-_GktEBGff8-WfSjYTy_Lz4lxtkUWvRz30gwrYYVpc7fz2WF57-0tV1i9ZnztzTsbpJPKAaUzZpTm8CPU-CwoE8dpqmhQ62CpqRM6JR7nZ4=s512

#data-origin-author

<p><strong>Gus Sonoda</strong>, Sr. Staff Motion Designer</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4fq3pk-Gus.jpg?alt=media

imageUrlFife: https://lh3.googleusercontent.com/vjjP3XL0c4hzRIvqQZnBLXUOvskIFTGdQv6R0VdT5aoT7ETD5e44_eCbd7_1XPAZRUuaRq6EfVDG1L3iArToYCLoY0IV7ihw-tL5RAMnvBSC=s512

<p>Material Design has an exciting new preview release — <a href="https://m3.material.io/blog/building-with-m3-expressive?utm_source=blog&amp;utm_medium=referral&amp;utm_campaign=IO25" target="_self">Material 3 Expressive</a>. In this latest version 1.4.0-alpha14 of Material 3, you get access to a new theming system: motion!</p><p>Previously, Material motion was defined through non-customizable easing and duration values. Today, we’re introducing a new, customizable motion scheme using motion physics defined through a set of motion properties. These can be customized or overridden as needed, giving you more control than ever over how motion works and feels in your product.</p><p>Read on to learn how the new motion physics scheme works, how existing APIs have changed, and how to get started.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4fuzya-Motion_Physics_16-9-aspect.mp4?alt=media

<h2>Why Material motion?</h2><p>As a product developer, you know that motion can significantly enhance the user experience. But achieving consistent motion across a complex app can be challenging. The new Material motion system solves this with:</p><ul><li><p><strong>Centralized control:</strong> Define your motion theme once, and all Material Components and even your own custom components will inherit it, creating a unified and polished experience, eliminating scattered animation specs.</p></li><li><p><strong>Simplified theming:</strong> Stop fussing with individual duration or easing values. Choose from predefined schemes or create your own, using physics-based spring animations for a natural and engaging feel.</p></li><li><p><strong>Adaptive animations:</strong> Ensure that movement feels fast in the context of the device and adjusts based on user input since animations are not based on predefined time sets.</p></li></ul>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4fyuj5-test.gif?alt=media

<h2>Getting setup</h2><p>First, make sure you’re using the latest version of Compose Material 3:</p>

androidx.compose.material3:material3:1.4.0-alpha11

<p>If you do nothing more than update the Compose dependency, your apps will benefit from applying the standard motion scheme to all your uses of Material Components. But if you do want that extra bit of control, you can customize your scheme to suit your app.</p><p><em>Note: When 1.4.0 goes to stable, the Material Expressive APIs will move to the next alpha (1.5.0-alphaX), and will no longer be available in 1.4.0. The APIs will go stable in the 1.5.0 release.</em> </p>

<h2>Fundamentals of the motion system</h2>

<h3>Motion schemes: Expressive or Standard</h3><p>The physics system has two preset motion schemes: <strong>Expressive</strong> and <strong>Standard</strong>. The scheme you choose will define how your product feels. While most motion in a product should use the same scheme, advanced customizations allow you to swap the scheme to emphasize key moments.</p><ul><li><p><strong>Expressive</strong> is Material’s recommended motion scheme, and should be used for most situations, particularly hero moments and key interactions.</p></li><li><p><strong>Standard,</strong> with its small amount of bounce, feels more functional and should be used for utilitarian products.</p></li></ul>

<p>Expressive: The Expressive motion scheme overshoots the final values to add bounce.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4g88ne-Scheme_Spring_Expressive_Export.mp4?alt=media

<p>Standard: The Standard motion scheme eases into the final values.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4g8yey-Scheme_Spring_Standard_Export.mp4?alt=media

<h2>Animation specs: Spatial or Effect</h2><p>Two distinct kinds of specifications make up the motion scheme: <strong>Spatial</strong> animation specs and <strong>Effect</strong> animation specs.</p>

<p><strong>Spatial</strong> specs are used to animate changes in an object's position, orientation, size, and shape. The spring overshoots the final value and bounces into place.</p>

<p>Spatial springs applied to movement.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4ge2fd-unnamed1.gif?alt=media

imageUrlFife: https://lh3.googleusercontent.com/CWMlcn4iysCXeyvgc4NYGXLGuYc3XxUX4r0sZxJb0R1YDks9HSC2hQptFExqmD7wCboG270-b7pgZ3zaP-fN8RusrH9iq3Dhh0Pj7_oclOlB=s328

<p>Spatial springs applied to rotation.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4gf1n5-unnamed2.gif?alt=media

imageUrlFife: https://lh3.googleusercontent.com/jQ-CxwzqRQJnmGKbSTD0CDhFD2NQTRKjd4bXZnKoEz1v-_BFuKvYlqacoBt4z3OUF_9WQpOaxcXONhlNWK7lnmE4_I6GA8p-ybdiddHyODpq=s328

<p><strong>Effect</strong> specs are used to animate an object’s properties such as color and opacity, where there shouldn’t be any overshoot.</p>

<p>Effects springs applied to opacity.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4ghub6-unnamed3.gif?alt=media

imageUrlFife: https://lh3.googleusercontent.com/EFgd_M-QGccSaDTuqe64lZDDdXZwZPylVH5nqsy1vnlI7U_sxvOycf8oEkeC7sm77p7E3Ok__1u5TCSapKdPvtLlpv8GIZaHa2ewZW52S0hT=s656

<p>Effects springs applied to color.</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4gjeks-unnamed4.gif?alt=media

imageUrlFife: https://lh3.googleusercontent.com/Bh3-_cViFNE23c15P8Ts_Nvtr0KKHUsfcSEOywGLhjSc3lAdN9xN7DygUt41oijdV3V5zkaw0FbACi3V6yMB3895X50UjWdG_CCkKbBKBh7MgQ=s328

<p>Each animation can also have one of three speeds: <strong>default</strong>, <strong>fast</strong>, and <strong>slow</strong>. Most motion should use the default speed, but smaller elements may benefit from the fast speed and larger elements from the slow.</p>

<div class="table-wrapper"><table class="borderGGrey400" style="width:100%"><tbody><tr><td><p>Speed</p></td><td><p>Spatial example</p></td><td><p>Effects example</p></td></tr><tr><td><p>Default</p></td><td><p>Animations that partially cover the screen, such as <a href="/m3/pages/bottom-sheets/overview" target="_self">bottom sheets</a> or <a href="/m3/pages/navigation-rail/overview" target="_self">expanded navigation rails</a></p></td><td><p>Opacity of the content within a navigation rail</p></td></tr><tr><td><p>Fast</p></td><td><p>Animations for small components such as <a href="/m3/pages/switch/overview" target="_self">switches</a> and <a href="/m3/pages/common-buttons/overview" target="_self">buttons</a></p></td><td><p>Color change of the switch handle</p></td></tr><tr><td><p>Slow</p></td><td><p>Full-screen <a href="/m3/pages/motion-transitions/transition-patterns/" target="_self">animations</a></p></td><td><p>Full-screen content refresh</p></td></tr></tbody></table></div>

<p><strong>Speed tokens work across devices.</strong> For example, the <strong>Spatial “fast”</strong> token will always be faster than <strong>“default”</strong> or <strong>“slow,”</strong> but the exact values of each token will differ depending on whether the device is a wearable, phone, or tablet. This ensures the movement feels fast in the context of the device. This also applies when using spring tokens in a custom motion scheme.</p>

<p>Effects motion in fast, default, and slow speeds</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4hb41v-AllSpeeds_Standard_Export.mp4?alt=media

<p>Spatial motion in fast, default, and slow speeds</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4hc9vj-AllSpeeds_Expressive_Export.mp4?alt=media

<p>Notice that the Expressive and Standard schemes are presets of opinionated motion values. This makes it easier to swap schemes without changing the underlying property names.</p>

<p>Expressive and Standard MotionScheme</p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4hf2tf-unnamed5.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/smuf6EuWMbN77Hv3d_SunEmOcTz0ZeZWerftjSIgz2Aw55bwpI8yR5DSuq6YEqV5WrJVzWOFQPzmCLLexaDJYewcpnb0O4eu4OBanGqVo3XLFg=s1352

<h2>Why use motion springs?</h2><p>If you look at the predefined specifications on the motion schemes, you may notice that springs are used for the backing specifications. Why is this? Spring animations appear more natural by allowing for the ability to interrupt and retarget the animation when required.</p><p>For example, consider the difference between using tween and springs:</p>

<p>Tween interruptions.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4hkmsg-00_compare_tween.mp4?alt=media

<p>Spring interruptions.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4hqa7d-00_compare_spring.mp4?alt=media

<p>When interrupted and retargeted to a new destination, the spring animation uses its current velocity to perform a more seamless transition between the two states than tween.</p><p>It’s also beneficial to use springs to ensure your animations easily <strong>adapt to different screen sizes</strong>, as the tokens will always be slow or fast in the context of the device since it is not time that is specified  but rather damping and stiffness. For more details on the benefits of springs, check out the <a href="https://developer.android.com/develop/ui/compose/animation/customize?_gl=1*9ewdxh*_ga*MzI1NjMyOTExLjE3NjI0MTE3NDU.*_ga_QPQ2NRV856*czE3NzQzNDgyNDgkbzE3OCRnMCR0MTc3NDM0ODM1MCRqNjAkbDAkaDA.#spring?utm_source=blog&amp;utm_medium=motion&amp;utm_campaign=IO25" target="_blank">documentation</a>.</p>

<h2>Customizing your motion scheme</h2><p>The real power of the new system lies in its flexibility. You can tailor the motion scheme to reflect your app’s brand or to underscore an important interaction.</p>

<h3>Choosing between Standard and Expressive schemes</h3><p>Most developers won’t want to change much in terms of motion theming, but there are two out-of-the-box options for you to choose from: <span class="inline-code">Standard</span> or <span class="inline-code">Expressive</span>. Choosing <span class="inline-code">MaterialExpressiveTheme</span> at the top level will default to the <span class="inline-code">Expressive</span> motion scheme.</p><p>Make this choice once for your application at the theme level, and any Material Components with movement built in will use the selected spec from the theme.</p>

@Composable
fun YourCustomTheme(){
   MaterialExpressiveTheme(
      motionScheme = MotionScheme.expressive(), // or MotionScheme.standard() 
   ) {

   }
}

<p>With the <span class="inline-code">expressive()</span> scheme your apps take on the Material-recommended motion scheme, whereas with the <span class="inline-code">standard()</span>, the motion is, well, pretty standard — there is a minimal amount of bounce, even as both use springs under the hood.</p>

<h3>Creating your own Motion scheme</h3><p>For more fine-grained control, you can create your own <span class="inline-code">MotionScheme</span> object and return a different <span class="inline-code">AnimationSpec</span> for each property.</p><p>In the code snippet below, we create a whole new <span class="inline-code">playfulMotionScheme</span> that by default adds a lot of bounce to components. This demonstrates how you can customize your <span class="inline-code">MotionScheme</span>.</p>

@ExperimentalMaterial3ExpressiveApi
fun playfulMotionScheme(): MotionScheme =
    object : MotionScheme {

        override fun <T> defaultEffectsSpec(): FiniteAnimationSpec<T> {
            return spring(
                dampingRatio = Spring.DampingRatioNoBouncy,
                stiffness = 1600f
            )
        }

        override fun <T> defaultSpatialSpec(): FiniteAnimationSpec<T> {
            return spring(dampingRatio = 0.6f, stiffness = 700f)
        }

        override fun <T> fastEffectsSpec(): FiniteAnimationSpec<T> {
            return spring(dampingRatio = Spring.DampingRatioNoBouncy, stiffness = 3800f)
        }

        override fun <T> fastSpatialSpec(): FiniteAnimationSpec<T> {
            return spring(dampingRatio = 0.6f, stiffness = 1400f)
        }

        override fun <T> slowEffectsSpec(): FiniteAnimationSpec<T> {
            return spring(dampingRatio = Spring.DampingRatioNoBouncy, stiffness = 800f)
        }

        override fun <T> slowSpatialSpec(): FiniteAnimationSpec<T> {
            return spring(dampingRatio = 0.6f, stiffness = 300f)
        }
    }


// To use the scheme: In your top level composable

@Composable
fun MyCustomTheme(
    //... other theme properties
    content: @Composable () -> Unit
) {
    MaterialExpressiveTheme(
        //.... other theme properties
        motionScheme = playfulMotionScheme(),
        content = {
            content()
        }
    )
}

<p>FAB menu with an extra-stiff custom scheme.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4lh9wb-Customization_Fab_Instant_Export.mp4?alt=media

<p>FAB menu with very low stiffness custom scheme.</p>

videoUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4ligvz-Customization_Fab_Soft_Export.mp4?alt=media

<h2>Custom component animations</h2><p>To maintain consistency with other Material Components, ensure your custom components adopt the recommended motion changes and use the motion specs available through <span class="inline-code">MaterialTheme.motionScheme</span>.</p><p>For example, the following code uses <span class="inline-code">tween()</span> calls to animate the size and color of a text component when pressing and releasing its container:</p>

val interactionSource = remember { MutableInteractionSource() }
val isPressed by interactionSource.collectIsPressedAsState()
val scale by
  animateFloatAsState(
      targetValue = if (isPressed) 8f else 1f,
      animationSpec = tween(1000),
      label = "scale"
  )
val color by
  animateColorAsState(
      targetValue = if (isPressed) Color.Green else Color.Red,
      animationSpec = tween(1000),
      label = "color"
  )
Box(
  modifier =
      Modifier.fillMaxSize().clickable(
          interactionSource = interactionSource,
          indication = null
      ) {}
) {
  Text(
      text = "Hello",
      modifier =
          Modifier.graphicsLayer {
                  scaleX = scale
                  scaleY = scale
                  transformOrigin = TransformOrigin.Center
              }
              .align(Alignment.Center),
      style = LocalTextStyle.current.copy(color = color, textMotion = TextMotion.Animated)
  )
}

<p>Since <span class="inline-code">scale</span> represents a <span class="inline-code">Spatial</span> motion and <span class="inline-code">color</span> falls under <span class="inline-code">Effects</span> motion, we can leverage the motion scheme for consistent application. This approach aligns your component’s motion to the overall app experience and allows it to adapt automatically when switching between <span class="inline-code">Standard</span> and <span class="inline-code">Expressive</span> schemes/themes.</p>

val interactionSource = remember { MutableInteractionSource() }
val isPressed by interactionSource.collectIsPressedAsState()
val scale by
  animateFloatAsState(
      targetValue = if (isPressed) 8f else 1f,
      animationSpec = MaterialTheme.motionScheme.defaultSpatialSpec<Float>(),
      label = "scale"
  )
val color by
  animateColorAsState(
      targetValue = if (isPressed) Color.Green else Color.Red,
      animationSpec = MaterialTheme.motionScheme.defaultEffectsSpec<Color>(),
      label = "color"
  )
Box(
  modifier =
      Modifier.fillMaxSize().clickable(
          interactionSource = interactionSource,
          indication = null
      ) {}
) {
  Text(
      text = "Hello",
      modifier =
          Modifier.graphicsLayer {
                  scaleX = scale
                  scaleY = scale
                  transformOrigin = TransformOrigin.Center
              }
              .align(Alignment.Center),
      style = LocalTextStyle.current.copy(color = color, textMotion = TextMotion.Animated)
  )
}

<h2>Individual Material Component changes</h2><p>In the expressive update, most Material 3 components use the motion physics system by default.</p><p>To add the motion-physics system to other components, including those that are custom built, use the specifications from above. See the full <a href="https://m3.material.io/blog/building-with-m3-expressive?utm_source=blog&amp;utm_medium=motion&amp;utm_campaign=IO25" target="_self">M3 Expressive announcement blog post</a> for more details on the new components.</p>

<h2>Get started today</h2><p>Try out the new motion subsystem in Material 3 Expressive today, and let us know how you like it by tagging us on social media @GoogleDesign. If you find any issues, please file them on the <a href="https://b.corp.google.com/issues/new?component=742043&amp;template=1590761?utm_source=blog&amp;utm_medium=referral&amp;utm_campaign=IO25" target="_blank">issue tracker</a>.</p><p>Happy theming!</p><p><em>Special thanks to Material motion designers Gus Winkelman and Gustavo Gonzalez.</em></p>

<h2>Up next</h2>

Start building with M3 Expressive

<p></p>

imageUrl: https://firebasestorage.googleapis.com/v0/b/design-spec/o/projects%2Fm3%2Fimages%2Fmn4mdykz-unnamed6.png?alt=media

imageUrlFife: https://lh3.googleusercontent.com/E8P9pn11UtnXLi0_Z6sTHj6pSGtQkWwp22TnH_X5oq60j9QvUXka915aeitDVb7yWMLSKO-J3KNGZJ8BZLyJfi8WmN68NvrKTjZzQ4KD2POQ6Q=s512

linkUrl: https://m3.material.io/blog/building-with-m3-expressive
