- 👋 Hi, I’m @NamanSaini18
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...

<!---
NamanSaini18/NamanSaini18 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result = []
    for i in range (x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k != n:
                    result.append([i,j,k])
    print(result)
