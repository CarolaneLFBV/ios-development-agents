# UIKit and SwiftUI interoperation

Preserve UIKit in existing or explicitly requested UIKit/hybrid screens. For pure
UIKit work, follow the project's controller lifecycle, containment, layout,
navigation and delegate patterns; do not migrate the screen just to use this skill.
Keep view/controller changes on the appropriate UI isolation domain.

For `UIViewRepresentable`/`UIViewControllerRepresentable`, separate creation from
updates. Updates may run repeatedly: avoid duplicate observers, targets, delegates,
constraints or expensive work. Update coordinator state/callbacks when parent inputs
change; a coordinator capturing the initial representable can retain stale values.
Synchronize binding/delegate changes without a feedback loop or mutation during
SwiftUI's rendering update.

Use the teardown hook to remove observers and targets, cancel owned work, release
delegates when appropriate and balance child-controller containment. Clarify which
component owns every callback/resource and justify weak captures from that graph.

Respect the hosting framework's sizing contract. Do not directly mutate the hosted
UIView's frame/bounds/center/transform when SwiftUI owns layout. Use supported sizing
or constraints and test repeated updates, resizing, Dynamic Type, navigation and
removal/recreation. App-wide lifecycle, background events and extensions belong to
platform integration; this reference owns the UI bridge itself.
[UIViewRepresentable](https://developer.apple.com/documentation/swiftui/uiviewrepresentable),
[UIViewControllerRepresentable](https://developer.apple.com/documentation/swiftui/uiviewcontrollerrepresentable).
