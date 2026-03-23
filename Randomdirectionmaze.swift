import SwiftUI

struct ContentView: View {
    // State variable to store the result of the random choice
    @State private var resultText: String = "Press the button!"
    
    // Your list of options
    let options = ["left", "right", "up", "down"]
    
    var body: some View {
        VStack(spacing: 30) {
            Text("Direction Randomizer")
                .font(.headline)
                .foregroundColor(.secondary)
            
            // The display area for the random string
            Text(resultText)
                .font(.system(size: 40, weight: .bold, design: .rounded))
                .transition(.opacity)
                .id(resultText) // Forces animation when text changes
            
            // The software button
            Button(action: {
                generateRandomDirection()
            }) {
                Text("Generate")
                    .font(.title2)
                    .fontWeight(.semibold)
                    .frame(width: 200, height: 60)
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(15)
                    .shadow(radius: 5)
            }
        }
        .padding()
    }
    
    // Logic to pick a random item from the array
    func generateRandomDirection() {
        if let randomChoice = options.randomElement() {
            withAnimation {
                resultText = randomChoice
            }
        }
    }
}

#Preview {
    ContentView()
}
