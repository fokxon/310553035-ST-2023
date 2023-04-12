/*
  Ref:
  * https://llvm.org/doxygen/
  * https://llvm.org/docs/GettingStarted.html
  * https://llvm.org/docs/WritingAnLLVMPass.html
  * https://llvm.org/docs/ProgrammersManual.html
 */
#include "lab-pass.h"
#include "llvm/IR/LegacyPassManager.h"
#include "llvm/IR/Module.h"
#include "llvm/IR/BasicBlock.h"
#include "llvm/IR/IRBuilder.h"
#include "llvm/IR/Constants.h"
#include "llvm/IR/Type.h"

#include <string>
#include <vector>

using namespace llvm;

char LabPass::ID = 0;

bool LabPass::doInitialization(Module &M)
{
  return true;
}

static Constant *getI8StrVal(Module &M, char const *str, Twine const &name)
{
  LLVMContext &ctx = M.getContext();

  Constant *strConstant = ConstantDataArray::getString(ctx, str);

  GlobalVariable *gvStr = new GlobalVariable(M, strConstant->getType(), true,
                                             GlobalValue::InternalLinkage, strConstant, name);

  Constant *zero = Constant::getNullValue(IntegerType::getInt32Ty(ctx));
  Constant *indices[] = {zero, zero};
  Constant *strVal = ConstantExpr::getGetElementPtr(Type::getInt8PtrTy(ctx),
                                                    gvStr, indices, true);

  return strVal;
}

static FunctionCallee printfPrototype(Module &M)
{
  LLVMContext &ctx = M.getContext();

  FunctionType *printfType = FunctionType::get(
      Type::getInt32Ty(ctx),
      {Type::getInt8PtrTy(ctx)},
      true);

  FunctionCallee printfCallee = M.getOrInsertFunction("printf", printfType);

  return printfCallee;
}

bool LabPass::runOnModule(Module &M)
{
  errs() << "runOnModule\n";

  LLVMContext &ctx = M.getContext();
  FunctionCallee printfCallee = printfPrototype(M);
  Constant *format = getI8StrVal(M, "%*s%s: %p\n", "format");
  Constant *space = getI8StrVal(M, "", "space");

  Constant *one = Constant::getIntegerValue(Type::getInt32Ty(ctx), APInt(32, 1, true));
  Constant *negOne = Constant::getIntegerValue(Type::getInt32Ty(ctx), APInt(32, -1, true));

  Type *i32Ty = Type::getInt32Ty(ctx);
  GlobalVariable *depth  = new GlobalVariable(M, i32Ty, false, GlobalValue::ExternalLinkage, ConstantInt::get(i32Ty, 0), "depth");

  for (auto &F : M)
  {
    if (F.empty()) {
      continue;
    }

    errs() << F.getName() << "\n";

    BasicBlock &Bstart = F.front();
    BasicBlock &Bend = F.back();

    // Insert code at prologue
    Instruction &Istart = Bstart.front();
    IRBuilder<> BuilderStart(&Istart);

    Value *myDepth = BuilderStart.CreateLoad(i32Ty, depth);
    Value *res = BuilderStart.CreateAdd(myDepth, one);
    BuilderStart.CreateStore(res, depth);

    Constant* name = BuilderStart.CreateGlobalStringPtr(F.getName());
    std::vector<llvm::Value*> args;
    args.push_back(format);
    args.push_back(myDepth);
    args.push_back(space);
    args.push_back(name);
    args.push_back(&F);
    BuilderStart.CreateCall(printfCallee, args);

    // Insert code at epilogue
    Instruction &Iend = Bend.back();
    IRBuilder<> BuilderEnd(&Iend);

    myDepth = BuilderEnd.CreateLoad(i32Ty, depth);
    res = BuilderEnd.CreateAdd(myDepth, negOne);
    BuilderEnd.CreateStore(res, depth);
    // TODO
  }

  return true;
}

static RegisterPass<LabPass> X("labpass", "Lab Pass", false, false);