import StoreKit

@MainActor
final class PurchaseController {
    var premium = UserDefaults.standard.bool(forKey: "premium")
    var listener: Task<Void, Never>?

    func showPaywall() {
        listener = Task {
            for await result in Transaction.updates {
                guard case .verified(let transaction) = result else { continue }
                premium = transaction.expirationDate.map { $0 > Date() } ?? true
                await transaction.finish()
            }
        }
    }

    func hidePaywall() { listener?.cancel() }

    func buy(_ product: Product) async throws {
        let result = try await product.purchase()
        if case .success(let verification) = result {
            premium = true
            UserDefaults.standard.set(true, forKey: "premium")
            await verification.unsafePayloadValue.finish()
        }
    }
}
