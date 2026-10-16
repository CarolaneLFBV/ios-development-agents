import SwiftUI

struct ProfileCard: View {
    let name: String
    let save: () -> Void

    var body: some View {
        HStack {
            Text(name).font(.system(size: 14)).lineLimit(1)
            Button(action: save) { Image(systemName: "checkmark") }
        }
        .frame(height: 32)
    }
}
