import SwiftUI
import UIKit

struct EditorBridge: UIViewRepresentable {
    @Binding var text: String

    func makeCoordinator() -> Coordinator { Coordinator(self) }
    func makeUIView(context: Context) -> UITextView { UITextView() }

    func updateUIView(_ view: UITextView, context: Context) {
        view.delegate = context.coordinator
        view.text = text
        view.frame = CGRect(x: 0, y: 0, width: 320, height: 80)
        NotificationCenter.default.addObserver(context.coordinator, selector: #selector(Coordinator.changed),
                                               name: UITextView.textDidChangeNotification, object: view)
    }

    final class Coordinator: NSObject, UITextViewDelegate {
        let parent: EditorBridge
        init(_ parent: EditorBridge) { self.parent = parent }
        @objc func changed(_ notification: Notification) {
            if let view = notification.object as? UITextView { parent.text = view.text }
        }
    }
}
