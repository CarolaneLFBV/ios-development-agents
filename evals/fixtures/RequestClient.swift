import Foundation

actor RequestClient {
    let session: URLSession
    init(session: URLSession) { self.session = session }

    func send(_ request: URLRequest) async throws -> Data {
        for _ in 0..<10 {
            do {
                let (data, _) = try await session.data(for: request)
                return data
            } catch {
                try? await Task.sleep(for: .seconds(1))
            }
        }
        return Data()
    }
}
