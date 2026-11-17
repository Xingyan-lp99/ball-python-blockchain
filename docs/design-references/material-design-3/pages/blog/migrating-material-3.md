# Migrating to Material Design 3

Source: https://m3.material.io/blog/migrating-material-3
Content endpoint: https://m3.material.io/page-data/Posts/5025319425409024.json
Content version: 2026-11-17_08-50-14

This is an upstream documentation snapshot. HTML fragments and media URLs are preserved.

Authors

_f68a99ffe9144467a917320028f1ce3b_/_50ac3cbb26fa4c21a9967e26675f94c5_/e542d55e05d06e63bbf3dadd467d6f4889a15a6c2c43b46c812a48b6ee2adf7ff126e17cb0d3c04d4d2f24d216f00138ed4cd9cbf209538cb1bd0f4fd7ac7f15

https://lh3.googleusercontent.com/ECgal03qq-GPHfoWRZft82d97qPwwB-M4z1d-igDCWWAMWhJteOVP4HzaU2XhhQVfG9ME-_0DWTFA1eK28kgnTgTHBpSnTIhLK8TQKwE0zyq_lFckrs

James Williams

Material Developer Advocate

mio-example

```
import android.app.Application;
import com.google.android.material.color.DynamicColors;

public class MyApplication extends Application {
 @Override
 public void onCreate() {
   super.onCreate();
   // This is all you need.
   DynamicColors.applyToActivitiesIfAvailable(this);
 }
}
```

```
Navigation View bn = //... items.

// Retrieve the first menu item and increment the badge label MenuItem menuItem = bn.getMenu().getItem(0);

int menuItemId = menuItem.getItemId(); 
Badge Drawable badgeDrawable = bn.getOrCreateBadge(menuItemId);
// If the first menu item is selected and the badge was hidden, 
// call Badge Drawable #setVisible to ensure the badge is visible. 
badge Drawable.setVisible(true);
badge Drawable.setNumber(badgeDrawable.getNumber() +1);
```

<p>At Google I/O, we announced <a href="https://material.io/blog/announcing-material-you">Material You</a>, highlighting the most expressive personalization features in our latest iteration of the Material Design system, Material Design 3. Along with support for dynamic color, we&rsquo;ve also updated several Material Components.</p>
<p>Ready to migrate to Material Design 3? Let&rsquo;s get started!</p>
<h2>Migrating from M2 to M3 (MDC 1.4.0 to MDC 1.5.0)</h2>
<h4>Updating your theme to Material 3</h4>
<p>Material Design 3 has an expanded color system that takes advantage of features such as dynamic color.</p>
<p>If you use <a href="http://material.io/material-theme-builder" target="_blank" rel="noopener">Material Theme Builder</a> to reconfigure your palettes, you can simply drop in the Android XML or Compose theme code. Otherwise, replace <code>Theme.MaterialComponents.*</code> with <code>Theme.Material3.*</code> for themes and <code>Widget.MaterialComponents.*</code> with <code>Widget.Material3.*</code> for widget styles.</p>
<h2>Colors and Themes</h2>
<p>Themes in Material You expand the color space of its predecessors, adding a Tertiary color and a number of interpolated colors derived from the Primary, Secondary, Tertiary, and Error colors.</p>
<p>Full version:</p>
<p><span id="docs-internal-guid-85a05fcd-7fff-beb5-2d08-98dd0c14a10b"></span></p>
<div dir="ltr" align="left">
<table style="border-collapse: collapse; width: 37.2134%; height: 1620px; border-color: initial; border-style: none;" border="1" cellpadding="0"><colgroup><col style="width: 47.0297%;" width="169" /><col style="width: 52.7228%;" width="180" /></colgroup>
<tbody>
<tr style="height: 54px;">
<td style="height: 54px;">
<p dir="ltr"><strong>MDC 1.4.0</strong></p>
</td>
<td style="height: 54px;">
<p dir="ltr"><strong>Material 3</strong></p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">
<p dir="ltr">android:backgroundColor</p>
</td>
<td style="height: 54px;">
<p dir="ltr">android:backgroundColor</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">
<p dir="ltr">colorPrimary</p>
</td>
<td style="height: 54px;">
<p dir="ltr">colorPrimary</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">
<p dir="ltr">colorOnPrimary</p>
</td>
<td style="height: 54px;">
<p dir="ltr">colorOnPrimary</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">&nbsp;</td>
<td style="height: 54px;">
<p dir="ltr">colorPrimaryContainer</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">&nbsp;</td>
<td style="height: 54px;">
<p dir="ltr">colorOnPrimaryContainer</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">&nbsp;</td>
<td style="height: 54px;">
<p dir="ltr">colorPrimaryInverse</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">
<p dir="ltr">colorPrimaryVariant</p>
</td>
<td style="height: 54px;">
<p dir="ltr">DEPRECATED</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">
<p dir="ltr">colorPrimarySurface</p>
</td>
<td style="height: 54px;">
<p dir="ltr">colorSurface</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">
<p dir="ltr">colorOnPrimarySurface</p>
</td>
<td style="height: 54px;">
<p dir="ltr">colorOnSurface</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">
<p dir="ltr">colorSecondary</p>
</td>
<td style="height: 54px;">
<p dir="ltr">colorSecondary</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">
<p dir="ltr">colorOnSecondary</p>
</td>
<td style="height: 54px;">
<p dir="ltr">colorOnSecondary</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">&nbsp;</td>
<td style="height: 54px;">
<p dir="ltr">colorSecondaryContainer</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">&nbsp;</td>
<td style="height: 54px;">
<p dir="ltr">colorOnSecondaryContainer</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">
<p dir="ltr">colorSecondaryVariant</p>
</td>
<td style="height: 54px;">
<p dir="ltr">DEPRECATED</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">&nbsp;</td>
<td style="height: 54px;">
<p dir="ltr">colorTertiary</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">&nbsp;</td>
<td style="height: 54px;">
<p dir="ltr">colorOnTertiary</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">&nbsp;</td>
<td style="height: 54px;">
<p dir="ltr">colorTertiaryContainer</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">&nbsp;</td>
<td style="height: 54px;">
<p dir="ltr">colorOnTertiaryContainer</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">
<p dir="ltr">colorError</p>
</td>
<td style="height: 54px;">
<p dir="ltr">colorError</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">
<p dir="ltr">colorOnError</p>
</td>
<td style="height: 54px;">
<p dir="ltr">colorOnError</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">&nbsp;</td>
<td style="height: 54px;">
<p dir="ltr">colorErrorContainer</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">&nbsp;</td>
<td style="height: 54px;">
<p dir="ltr">colorOnErrorContainer</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">
<p dir="ltr">colorSurface</p>
</td>
<td style="height: 54px;">
<p dir="ltr">colorSurface</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">
<p dir="ltr">colorOnSurface</p>
</td>
<td style="height: 54px;">
<p dir="ltr">colorOnSurface</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">&nbsp;</td>
<td style="height: 54px;">
<p dir="ltr">colorSurfaceVariant</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">&nbsp;</td>
<td style="height: 54px;">
<p dir="ltr">colorOnSurfaceVariant</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">&nbsp;</td>
<td style="height: 54px;">
<p dir="ltr">colorSurfaceInverse</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">&nbsp;</td>
<td style="height: 54px;">
<p dir="ltr">colorOnSurfaceInverse</p>
</td>
</tr>
<tr style="height: 54px;">
<td style="height: 54px;">&nbsp;</td>
<td style="height: 54px;">
<p dir="ltr">colorOutline</p>
</td>
</tr>
</tbody>
</table>
</div>
<p></p>
<p>These new color spaces enable dynamic color expression. We&rsquo;ve made it easy to visualize dynamic color and migrate to our new color system with the <a href="http://material.io/material-theme-builder">Material Theme Builder</a>, available on the web and Figma. When generated via our tooling, these intermediate color values can be created by providing as little as one color.</p>
<p>&lt;mio-image index=0&gt;&lt;/mio-image&gt;</p>
<h2>How it works</h2>
<p>When a user changes their wallpaper on an Android 12 device, the image is analyzed to select a color and algorithmically choose Primary, Secondary, Tertiary, and Error colors using an initial seed color. At the same time it&rsquo;s applying color theory and accessibility rules. From these colors, the algorithm creates tonal palettes ranging from 0% luminance (BLACK) to 100% (WHITE). Dynamic theming or custom theming created through our tooling will use values in these tonal palettes to set the theme attributes for that color range.</p>
<p>&lt;mio-col-set cols=2&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=1&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=2&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;/mio-col-set&gt;</p>
<p><span id="docs-internal-guid-286220ee-7fff-7796-ab7b-ad834e8337f3"></span></p>
<p>For example, if the On Primary color, for text/icons shown on the Primary color is a 100 tone, then On Secondary, On Tertiary, and On Error will all be 100 tones in their respective colors for the light theme and perhaps 20 tone for the dark theme.</p>
<p>You are free to customize any of these values but be mindful of contrast and accessibility.</p>
<p>On Android 12 devices, Material You will generate dynamic palettes based on the user's wallpaper. In addition to the generated tonal palettes, there will be several pre-created schemes. To opt into dynamic colors, you need to make sure there aren't any hardcoded colors in your app. Instead, all colors in your app should be referenced as theme attributes, that way they can be easily swapped when enabling dynamic wallpaper color support.</p>
<h2>Integrating dynamic color</h2>
<p>The <code>DynamicColors</code> class from the Material library taps into Activity Lifecycle Callbacks to determine when and how to apply color overlays. Using the supplied API calls, you can apply dynamic color to a subset or the entire app. You can also determine when and where dynamic color should be applied.</p>
<p>To avoid unintended effects, you should make sure your application code references theme attributes and not any hard coded colors (HEX codes or @color/).</p>
<p>Given an app that uses a Material3 theme with MDC components, below is the minimum code you&rsquo;d need to enable dynamic color - a line in the <code>onCreate</code> method of your Application class.</p>
<p>&lt;mio-code-snippet index=0&gt;&lt;/mio-code-snippet&gt;</p>
<p>You can read more about our <a href="http://m3.material.io/libraries/mdc-android/color-theming" target="_blank" rel="noopener">color theming</a>. Follow along in our <a href="https://goo.gle/apply-dynamic-color" target="_blank" rel="noopener">Applying Dynamic Color codelab</a> to learn how to apply dynamic color in your app.</p>
<h2>Typography</h2>
<p>Typography styles have undergone a simplification. Before Material 3, there were 6 Headline variations, 2 Subtitle variations, 2 Body variations, Button, Caption, and Overline styles.</p>
<p>&lt;mio-col-set cols=2&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=3&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=4&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;/mio-col-set&gt;</p>
<p>In Material 3, there is a more regular and smaller number of variants for each classification, namely Small, Medium, and Large.</p>
<p>&lt;mio-col-set cols=2&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=5&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=6&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;/mio-col-set&gt;</p>
<p>Most of the new <code>TextAppearance</code> styles map directly to pre-Material 3 styles.&nbsp;The property names in MDC-Android are formed using a similar pattern: <code>textAppearance</code> + {Display, Headline, Title, Body, Label} + {Large, Medium, Small}</p>
<p><span id="docs-internal-guid-3657526f-7fff-5ed8-e116-e5b51cdc8cb8"></span></p>
<div dir="ltr" align="left">
<table style="border-collapse: collapse; border-color: #000000; border-style: solid;"><colgroup><col width="200" /><col width="220" /></colgroup>
<tbody>
<tr>
<td>
<p dir="ltr"><strong>New Property</strong></p>
</td>
<td>
<p dir="ltr"><strong>Old Property</strong></p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">textAppearanceDisplayLarge</p>
</td>
<td>
<p dir="ltr">textAppearanceDisplay2</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">textAppearanceDisplayMedium</p>
</td>
<td>
<p dir="ltr">textAppearanceDisplay3</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">textAppearanceDisplaySmall</p>
</td>
<td>
<p dir="ltr">textAppearanceHeadline1</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">textAppearanceHeadlineLarge</p>
</td>
<td>
<p dir="ltr">textAppearanceHeadline2</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">textAppearanceHeadlineMedium</p>
</td>
<td>
<p dir="ltr">textAppearanceHeadline3</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">textAppearanceHeadlineSmall</p>
</td>
<td>
<p dir="ltr">textAppearanceHeadline4</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">textAppearanceTitleLarge</p>
</td>
<td>
<p dir="ltr">textAppearanceHeadline5</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">textAppearanceTitleMedium</p>
</td>
<td>
<p dir="ltr">textAppearanceSubhead1/Subtitle1</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">textAppearanceTitleSmall</p>
</td>
<td>
<p dir="ltr">textAppearanceSubhead2/Subtitle2</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">textAppearanceBodyLarge</p>
</td>
<td>
<p dir="ltr">textAppearanceBody1</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">textAppearanceBodyMedium</p>
</td>
<td>
<p dir="ltr">textAppearanceBody2</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">textAppearanceBodySmall</p>
</td>
<td>
<p dir="ltr">textAppearanceCaption</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">textAppearanceLabelLarge</p>
</td>
<td>
<p dir="ltr">textAppearanceButton</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">textAppearanceLabelMedium</p>
</td>
<td>
<p dir="ltr">textAppearanceOverline</p>
</td>
</tr>
<tr>
<td>
<p dir="ltr">textAppearanceLabelSmall</p>
</td>
<td>
<p dir="ltr">N/A</p>
</td>
</tr>
</tbody>
</table>
</div>
<p>Read more about <a href="http://m3.material.io/libraries/mdc-android/typography-theming">Typography</a>.</p>
<h2>Component Updates</h2>
<h4>Top App Bar</h4>
<p>Top app bars have undergone a Material You refresh to better align with color. Before Material You, top app bars used shadow to differentiate between the app bar and content. Color is now the primary indicator of elevation using newly created surface tones.</p>
<p>&lt;mio-col-set cols=2&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=7&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=8&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;/mio-col-set&gt;</p>
<p>Read about <a href="https://github.com/material-components/material-components-android/blob/master/docs/components/TopAppBar.md" target="_blank" rel="noopener">implementing Top App Bar</a> with more examples and code snippets.</p>
<h4>Navigation Bar / Bottom Navigation View</h4>
<p>Bottom Navigation View has undergone a visual refresh and gained some new functionality. Currently each menu item in a Bottom Navigation View is composed of an icon and text label. When a destination is selected, both the icon and label will be tinted a different color from the inactive state.</p>
<p>&lt;mio-col-set cols=2&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=9&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=10&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;/mio-col-set&gt;</p>
<p>In Material Design 3, inactive destinations are indicated by an outlined version of the icon if available. Active destinations are indicated by a filled icon enclosed in a pill shaped container.</p>
<p>If distinct filled and outlined variants of an icon are not available, you may want to consider other cues to help indicate active state such as showing destination labels only on active destinations. Read about <a href="http://m3.material.io/components/navigation-bar/implementation/android" target="_blank" rel="noopener">implementing Navigation Bar</a> with more examples and code snippets.</p>
<h4>Floating Action Button</h4>
<p><code>FloatingActionButton</code> has undergone a bit of a redesign. FABs with no explicit theme or a legacy <code>Widget.Design.FloatingActionButton</code> theme will inherit this new design in a <code>Theme.Material3.*</code> theme.</p>
<p>The new FAB has less corner radius and now resembles a rounded rectangle versus the circular shape of existing FABs. There are preset styles to theme your FAB using tones from the Primary color, Secondary color, or surface color. To retain the former design for your Floating Action Buttons, make sure to set your FAB&rsquo;s style as <code>@style/Widget.MaterialComponents.FloatingActionButton</code>. There is also a new large FAB variant. Read about <a href="http://m3.material.io/components/floating-action-button/implementation/android" target="_blank" rel="noopener">implementing FABs</a> with more examples and code snippets.</p>
<p>&lt;mio-col-set cols=2&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=11&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=12&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;/mio-col-set&gt;</p>
<h4>Buttons</h4>
<p>Filled and Outlined Buttons in Material Design 3 have fully rounded corners. Button widgets will auto-inflate to Material Button and apply a Material3 style if enclosed in a theme deriving from <code>Theme.Material3.*</code>. Read about <a href="http://m3.material.io/components/buttons/implementation/android" target="_blank" rel="noopener">implementing Buttons</a> with more examples and code snippets.</p>
<p>&lt;mio-col-set cols=2&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=13&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=14&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;/mio-col-set&gt;</p>
<h4>Chips</h4>
<p>In Material 2, Chips had fully rounded corners, in Material 3 they have undergone a visual change and now have 8 dp corners. They all have 8 dp corners in Material 3. Read about <a href="http://m3.material.io/components/chips/implementation/android" target="_blank" rel="noopener">implementing Chips</a> with more examples and code snippets.</p>
<p>&lt;mio-col-set cols=2&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=15&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;mio-column&gt;</p>
<p>&lt;mio-image index=16&gt;&lt;/mio-image&gt;</p>
<p>&lt;/mio-column&gt;</p>
<p>&lt;/mio-col-set&gt;</p>
<h4>Badges</h4>
<p>Bottom Navigation View is now able to display an associated badge either as a filled shape or with a label. A badge can be anchored to one of the four corners of the icon by setting its gravity to one of the constants declared in <code>Badge Drawable.BadgeGravity </code>:</p>
<p><code>TOP_START</code></p>
<p><code>TOP_END</code></p>
<p><code>BOTTOM_START</code></p>
<p><code>BOTTOM_END</code></p>
<p>Here is some code showing how to add badges to BottomNavigationView menu items:</p>
<p>&lt;mio-code-snippet index=1&gt;&lt;/mio-code-snippet&gt;</p>
<p>Read about <a href="https://github.com/material-components/material-components-android/blob/master/docs/components/BadgeDrawable.md" target="_blank" rel="noopener">implementing BadgeDrawable</a> with more examples and code snippets.</p>
<h2>What&rsquo;s next?</h2>
<p>We&rsquo;ve gone through the major differences between MDC 1.4.0 and the 1.5.0 (Material Design 3) release.</p>
<p>We encourage you to upgrade your application&rsquo;s dependencies to understand and explore the new options that Material Design 3 provides to enhance your user experience using color.</p>
<p>As always, we encourage you to file <a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=bug&amp;template=bug_report.md&amp;title=%5BComponent+name%5D+Short+description+of+issue" target="_blank" rel="noopener">bug reports</a> and <a href="https://github.com/material-components/material-components-android/issues/new?assignees=&amp;labels=feature+request&amp;template=feature_request.md&amp;title=%5BComponent+name%5D+Short+description+of+request" target="_blank" rel="noopener">feature requests</a> on GitHub.</p>

Light theme color values

Light theme color values

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/7244f4ea18b14a8228bded8d0c5f6fc3d83bf20457542f4fb5ec286a2bbd7f45bdfcd768a4d5cadc8d5057b90746da5ae6b895b1e444ead215978948d0bbc6c7

https://lh3.googleusercontent.com/HGVCq_oaSTrQvpvrFYzs9TNAG97Lr-QjHKeXxipVYtY-sODY8JPcCdF_UaUzAKJJQUNhhxjvOK60L0sSK56TrEEc2z9xxpHyaianFs1OVVUhGMTM86I

Autogenerated color palette from wallpaper selection with purple background

Autogenerated color palette extracted from wallpaper selection

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/3dfb6ba04b537c3c8ba1259fb697aab9612ff52ed8a5e6afa39a417139851c1eb67fc7936105c93be2cb097ec2e08d9cb19e99a5201fcb23ca2b9d91cb038f58

https://lh3.googleusercontent.com/aPtfVrQXQU58mv5ErQlSP4FYKis2J24Wp4mSSXnLysg4__g42Ge5PpPxIoaGZIn7w2uqXGgkrTZrAAVVIlTXEyOwZB37kFrHRqmBxvqCPQPZjdWCc9uk

Autogenerated basic colors extracted from wallpaper selection with light green background

Autogenerated basic colors extracted from wallpaper

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/fa63356ec27c47f2b4adf441f3b834daca40a04c9541108fee44d0a9c9298fcd90a2a071bacfdd3613bc9f079c62d406079cd0f4983126b81053c709c556511c

https://lh3.googleusercontent.com/jW2Qbm_nwdr7y6MxH6hs_HzibbQD1N_mO931aVJrkUUoOeToDHWlfRFs_PN-grj_D3HbOxxCFP-UiF6MqWKUTTPMULb6HPXMd5jkOsqx3nAgv_FfyQ

M2 Typescale showing values for Headline 1 through Headline 6

M2 typescale

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/bdd16d0809b5caf77838eb7c95ca26888f0274a8cc7fb82faee3d620abd3c93b9abe00d6b3f2c362233f40b3e21730b06ac837b586fe03e2b3a63ea7374edae5

https://lh3.googleusercontent.com/ET4D0doMjFqboEUZAd-WslLtzaM6YqhHvGzEM1ttM0RCrZ0Z2oyJsjM08MbUgELpswhGTtGR2zTYMrvnZSOiPiC0EOYOZsfoB83ah-JSV_FJCodAwiI

M2 Typescale showing values for Headline 4 through Overline

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/8147f58a54d7e91b2cf6516794241835bfd06ad40089c2c677ad7985f792904e5d15b418a2f20f482bd1aba0915fc4d7646e07b0b749aecc9d4fee797ef4b152

https://lh3.googleusercontent.com/dAAXht0Y01Qr0C9l9iMc3BW8dFyaPpKuf_6UEJKZq1kTInDFoAUKMjrt4R9vJBfbJTeRYGfkbHRuSjssOnf23lckjhsMWltNJVbqKsm-elOEeQKz4A

Material Design 3 typescale from Display to Title

M3 typescale

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/058539b8ab1f599598872a437fc7f14e6ffec30858f580930eac760b5d75e4411874210720e943eef9658a19112ffb70fdc978e602983b0795192d3571c6186d

https://lh3.googleusercontent.com/kwY9Q3Z1kaVabE9tCcnyhDWKd8tHH28K1Wpr745DpH1zAvQZN4JEJ_0MsdBsJIe56tQrvGVZ9MMf9lNl6ndnCcMbScna3JG5hjmPr7n48NhBJ8Gk8JE

Material Design 3 typescale from Headline to Label

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/1b151c9080adf08d3a9c66ff78d018094ff7db8a37195b27e7ebf79fdaf9364b6ddf81f38f46be659d96dd05d680444613305f59013656dfb42bab9ea040f2f8

https://lh3.googleusercontent.com/RhDetfwKACxoBvlRmKUeFReJoVq9f6wjkLv2Zo13qWlw4JTVw-yRCYsm0-5v0U61thnt70QT8gSVvC_ONuAMQJBD0pJecK4IDXMMbK8_K0jAgwpeP14

M2 example of top app bar

M2 example of top app bar

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/9cd7b99c82dfa777fdfb4bfef0fde8f0345289257ff8422e2362e87ef8f239d7c8b0a1ded13408279f9a740488e12dc25add6a9cd2be72d5614c073396f56655

https://lh3.googleusercontent.com/HXxxqSgn2IlhyyRd9TxO1K7Q5NjgeBCl6VvPjDUQAs99dRulWPBcqpNpWlunP7-esOp_Jx8vsBfMj0PcgSvx16Mmvc8H2YU0T0j3aSJ8T3uQZHgVaoo

M3 example of top app bar

M3 example of top app bar

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/cc99111817b18779ba3d703af8c6c158358cccbee11e96bb0f3898d4108ad216995a86aa5fd2549e554b748807b853c97a3212a48083a70ee15efa32ea0b30b0

https://lh3.googleusercontent.com/c3LorPvDAnYh6Z549nwclDrQgAqnKkmj-iFGE8D0ULD46vXUfVWdr3ULxvd_ql1Xaqlqn5kDZ6WRQioWxbq-y2nQa3NgDw-sDNig8kYx7lr8PitAN4c

M2 example of bottom navigation

M2 example of bottom navigation

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/1b363e7a672481b1a021456c0cdc1058d8e70ab1c6b6fd0e0d34c56c4a25997baaef7586de733ebf0a681d6ef889f1f444492d46603c9e705219f5730ef9cc52

https://lh3.googleusercontent.com/DonjATzMKbdXVwL1FyaG25BZAITuKRBa33uhJx4RlhfIajsCJMn6Gla2TPkUYOakuM30fAqBUpw21efKx0gpsirvT9lg1ooxxDt33EC_eJItHMay10g

M23example of bottom navigation

M3 example of bottom navigation

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/e90d50a47a0d6950714902d61da850e168d51dca814513a1aa8218dcf4d3b5ffd0924f11d12d1cb995a5ce19c5985a34378d39a804fed6386d5aa0079c431dac

https://lh3.googleusercontent.com/jM3cVRF4jiHr3FYQy7NV86X7idyBvc8LD211gvmxE-zzoDkihw82yjao4G6d26kM51DFSyo5GzFc6rFMI90QWthhn01TPGpKFQNEWkwAUWK3s0IF47s

M2 examples of Floating action buttons (FABs)

M2 examples of Floating action buttons (FABs)

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/f1d2d5163bab65d3c339f4c2fac003a89f716b67e987989584d34fcd5d5f321b04bbecc45dc3a59e5ba1aa60f821d1b8b90575e13e6b8682347d51cf27adc678

https://lh3.googleusercontent.com/jm-suA46gdE0qHH9BoEV7-TS_09xP4sWof0ar_wWyRH_DmRiRtncJ8MeQa_w-_MMwG9fmeDXBrSkFze2l6ByK2n-SPOLGhK1Vm7CJw6qpvO0RrPHEXc

M3 examples of Floating action buttons (FABs)

M3 examples of Floating action buttons (FABs)

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/8800b3a27af2422c391b46c30b9ea339084142a367e38a189860752bbbcf586634639e29ea4ecba746c4b7c6db360f003f31ac9ec6c05b5d2d33c731ae6192ab

https://lh3.googleusercontent.com/fzKDgTkU0tBYYGdXKMVais9mD6l3vOdbKcjkpQAffJiSiL3-i8v2vrRCOFiu5kF3fJ5iuv-KaDwznDlytH7P0K21-F7FCzAVDX3xPBpvY8UXDsuKw5c

M2 examples of buttons

M2 examples of buttons

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/f3e63dc0c580d9691729acc7a73d0c38a9ef118fcad348b8cfbcae0f1f48f5cd117652ae218435a8cd369312c387f7db97b7ddfc0da8226f3771e90f27ed1c31

https://lh3.googleusercontent.com/YWfToscYzCQQq7AjYDwqgv5Wfa85ql456eBs9-fjGJBteW-6EweuoJ8D3rw1J9N7CJr5w5tT2wW8qobvK9HbduoPW9ZMLt0M0PC-rgE9Gp_wfI2yFA4

M3 examples of buttons in purple light theme

M3 examples of buttons

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/17c08e380319706d3247c71e758950f28ff0e1969b896b4571ff5252176c7e9aa2abf3defc03ab1310e8a88cb67d69cf546889b9b9a16cb07988872a5c75466a

https://lh3.googleusercontent.com/1hVupzziJSxNwep8PPY7-eGramkOKZ0mfdWKY1z9UCOAJzhJGRXRJMiuIf2s4nx_Cik-ieB6lcxVJcpWS8B1xiHQDlxQS1GcG4-r-ElBlh0nE3ImoXM

M2 examples of chips

M2 examples of chips

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/02642f33fe0060a7d9577e9f418d6128ae07f47f7ad9b5c10e963725d16772fabef6a81f8b7af9406905be092d24c01ed0e228f89a0906db2055065341be7d2a

https://lh3.googleusercontent.com/ZogLjBR6FRroX1O7j9w2T0OcuMhTliMxHU-d9EJrFL1vYMAjWqkTbx_ZdncZOIevVIqdoHV_UZO6DerXWkGLDtYh73wFUjLSZH8A7KucjpP3JyH8vJem

M3 examples of chips

M3 examples of chips

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/4b739a04e2efde24edc07854d555a20d3286ea9271fde88474b867704e53e189878a9c1c956832df190d8e058e1179b41d3273270ed948b00503e0e87bf5b4d5

https://lh3.googleusercontent.com/Aj-AXipNMCWg65nokFv6mIb77dd82u0ZX9Jkf6tcxL7XQY0C-UqUSPI15OMzlw86P86tDE1VM4p2EamwcjKv5QJNzB9q6yPiCqOL_jnqTZO7jrljy9E

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/cd45afa251ec0b378409b71b086e7423a07f41358412241ecd50a11552e043c911fd63919c87e1df1ef308ab6b9a56b7cfbd17ffd2019fcc8d828a9d3e41e837

https://lh3.googleusercontent.com/KQ7Ul7smHbhue3rVhcE9xPIL7Dznf8eU7zEEnyevjyp39DBUPPNaI2kIAli81hdr3-f-jWH5O7N1zSvDh2rfVjHlwrmpLDpKbOj0tzcoPGyarxsMyYA

 

{}

Learn how to migrate to our newest updates

_f68a99ffe9144467a917320028f1ce3b_/_f3e8a4f639ce4c5aafa231fcb8daa630_/d6bbfe58d0c69c11ba925fd6b530d70946b4981bcb0b97c2578d94bf94cfd970546601a821cf79cba3c3286a3de8dbdff0bc1374062b316d8a184b1c361744b1

https://lh3.googleusercontent.com/ILbcgqsNOPqLX2Gd8uKQmLlGxIAoVsKSvJG1H0o3v2rlF4br-l9kEqjYNJCH0nnXa0KGlE9sXAfZ8M8BJQordWfl71eLOyySLYV6xhnsSmjPSyJ3gw

Migrating to Material Design 3

2021-10-27T09:20:00

migrating-material-3

Learn how to migrate to our newest updates

Migrating to Material Design 3

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/362302fcebd869d647a92554dbe8a7b1e06b1eeb8ce46a6e67bfc5403441aea79237facc6dfe929599f4fb4bc8e6e836d2efbccab8abed1fca121d67d244aac4

https://lh3.googleusercontent.com/rME0woOrBvWQqpvpmd_QteVRux9dw9pT7HhbEVneGV5yyo1WzljxXgwf4wynieJPHPs--tPySUe7uoMiJwuYj-oNzXC8PwwXE1wK7Dyv9_UDhyce5A

Start building with Material You

/blog/start-building-with-material-you

Start building with Material You

Material Blog

Start building with Material You

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/b14f83531e0ded0b48ab6c6e03d8645b76f3a34d7abe4a849ea689a09b0ab4dbd5b52ffda0e00d05c9cc3d0aafa490251c132c68911265a6b25b3b74cf67876a

https://lh3.googleusercontent.com/Aj_PgNvXar9dTxMmBoCjGE5OG1jhEZyjoXUI3mOJMdhY68LvL1LYuI5aL0r8e3lESTZWL6mqhRPY30qYd9VDIPx6lXdomuw4orxQ6T_mlAGJvggS6Bc

Introducing Material Theme Builder

/blog/material-theme-builder

Introducing Material Theme Builder

Material Blog

Introducing Material Theme Builder

mio-example

UpNextItems

_f68a99ffe9144467a917320028f1ce3b_/_67af19389b5f45048ff0f3b64759ab41_/264a443d1e54b4ff4827d1c22552881b81e2fa872f16d65d10a8720f512633cefd0e6f116318d75c4c9e6ecc158af2bca9ef5dde4f35bd9754a8fb2d2da49170

https://lh3.googleusercontent.com/79I_k3QufXk598pk_Rmgl011wP9DDnn-gkJY49XZ_2kDArzQnL_4rnitH2W8t-wLJT8L_SV7jXbpil6MGS-483LsurzCXyXjeQR1JDdeGL0i2lVnScY

Unveiling Material You

/blog/announcing-material-you

Unveiling Material You

Material Blog

Unveiling Material You

mio-example
