import Testing

@MainActor
final class Loader {
    var isLoading = false
    func load() async {
        isLoading = true
        await Task.yield()
        isLoading = false
    }
}

@MainActor
@Test func loadingState() async {
    let loader = Loader()
    let task = Task { await loader.load() }
    #expect(loader.isLoading)
    await task.value
}
