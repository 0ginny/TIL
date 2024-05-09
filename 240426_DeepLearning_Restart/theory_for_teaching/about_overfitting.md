# overfitting

과적합이란, 너무 많은 파라미터 학습으로, 일반화되어 새로운 데이터셋에선 예측이 맞지 않는 상태를 일컬음. 

** 추가로 underfitting은 학습이 부족해서, train, validataion 데이터셋에서 모두 학습이 잘 되지 않는 상태

### 어떻게 확인 할 수 있을까?

- 차원이 1,2 차원으로 작으면, 데이터를 시각화해서 찾을 수 있겠지
- 3차원 이상의 경우는 통계적으로 cross-validation을 통해서 평가를 할 수 있어.

## 어떻게 피할 수 있을까?
### Using cross-validataion(training/hold-out/test sets)
### Use regulariztion (L2, drop-out, data manipulations, early stoppping)

