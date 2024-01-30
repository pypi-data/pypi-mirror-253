# pyofilename

Windows와 macOS, Linux에서 안전한 파일명을 만듭니다.

순수 파이썬 구현을 보고 싶다면 [이 링크](https://github.com/ilotoki0804/pyfilename)를 참고하세요.

Rust에서 사용하기 위한 구현을 보고 싶다면 [이 링크](https://docs.rs/rsfilename/latest/rsfilename)를 참고하세요.

이 패키지는 파이썬에서 사용할 수 있는 Rust 바인딩입니다.

```python
import pyofilename as pf

to_safe_name("hello?.txt", "fullwidth")
```
