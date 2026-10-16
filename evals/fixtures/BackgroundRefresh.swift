import BackgroundTasks

final class RefreshCoordinator {
    func register() {
        BGTaskScheduler.shared.register(forTaskWithIdentifier: "com.example.refresh", using: nil) { task in
            Task {
                await self.refresh()
                task.setTaskCompleted(success: true)
            }
            task.expirationHandler = { task.setTaskCompleted(success: false) }
        }
    }

    func schedule() throws {
        let request = BGAppRefreshTaskRequest(identifier: "com.example.refresh")
        request.earliestBeginDate = Date(timeIntervalSinceNow: 15 * 60)
        try BGTaskScheduler.shared.submit(request)
    }

    private func refresh() async {
        // The app's existing asynchronous sync operation.
    }
}
